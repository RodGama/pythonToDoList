# Write your code here
from datetime import datetime, timedelta

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class ListaDeTarefasTable(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


def tarefas_do_dia():
    Session = sessionmaker(bind=engine)
    session = Session()
    today = datetime.today()
    rows = session.query(ListaDeTarefasTable).filter(ListaDeTarefasTable.deadline == today).all()
    if len(rows) != 0:
        print("Today " + str(datetime.today().day) + " " + str(today.strftime('%b')) + ":")
        for tarefa in rows:
            print(tarefa.task)
    else:
        print("Nothing to do!")


def adicionar_tarefas():
    print("Enter task")
    tarefa = str(input())
    print("Enter deadline")
    ano, mes, dia = str(input()).split("-")
    data = datetime(int(ano), int(mes), int(dia)).date()
    Session = sessionmaker(bind=engine)
    session = Session()
    new_row = ListaDeTarefasTable(task=tarefa, deadline=data)
    session.add(new_row)
    session.commit()
    print("The task has been added!")


def todas_as_tarefas():
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(ListaDeTarefasTable).all()
    if len(rows) != 0:
        count = 1
        for tarefa in rows:
            print(str(count) + ". " + tarefa.task + ". " + str(tarefa.deadline.day) + " " + str(
                tarefa.deadline.strftime('%b')) + "")
            count += 1
        print()
    else:
        print("Nothing to do!\n")


def tarefas_da_semana():
    Session = sessionmaker(bind=engine)
    session = Session()
    today = datetime.today()
    for dia in range(7):
        data_pesquisa = today + timedelta(days=dia)
        rows = session.query(ListaDeTarefasTable).filter(ListaDeTarefasTable.deadline == data_pesquisa.date()).all()
        if data_pesquisa.weekday() == 0:
            dia_da_semana = "Monday"
        elif data_pesquisa.weekday() == 1:
            dia_da_semana = "Tuesday"
        elif data_pesquisa.weekday() == 2:
            dia_da_semana = "Wednesday"
        elif data_pesquisa.weekday() == 3:
            dia_da_semana = "Thursday"
        elif data_pesquisa.weekday() == 4:
            dia_da_semana = "Friday"
        elif data_pesquisa.weekday() == 5:
            dia_da_semana = "Saturday"
        elif data_pesquisa.weekday() == 6:
            dia_da_semana = "Sunday"
        print(dia_da_semana + " " + str(data_pesquisa.day) + " " + str(today.strftime('%b')) + ":")
        if len(rows) != 0:
            count = 1
            for tarefa in rows:
                print(str(count) + ". " + tarefa.task)
                count += 1
            print()
        else:
            print("Nothing to do!\n")


def deletar_tarefa():
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(ListaDeTarefasTable).order_by(ListaDeTarefasTable.deadline).all()
    print("Chose the number of the task you want to delete:")
    if len(rows) != 0:
        count = 1
        for tarefa in rows:
            print(str(count) + ". " + tarefa.task + ". " + str(tarefa.deadline.day) + " " + str(
                tarefa.deadline.strftime('%b')) + "")
            count += 1
        print()
    else:
        print("Nothing to delete!\n")
    tarefa = int(input())
    linha = session.query(ListaDeTarefasTable).filter(ListaDeTarefasTable.id < rows[tarefa].id).all()
    specific_row = linha[0]
    session.delete(specific_row)
    session.commit()
    print("The task has been deleted!")

def tarefas_perdidas():
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(ListaDeTarefasTable).filter(ListaDeTarefasTable.deadline < datetime.today()).all()
    if len(rows) != 0:
        print("Missed tasks:")
        count = 1
        for tarefa in rows:
            print(str(count) + ". " + tarefa.task + ". " + str(tarefa.deadline.day) + " " + str(
                tarefa.deadline.strftime('%b')) + "")
            count += 1
        print()
    else:
        print("Nothing is missed!")


def menu():
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")
    acao = int(input())
    while acao != 0:
        if acao == 1:
            tarefas_do_dia()
        elif acao == 2:
            tarefas_da_semana()
        elif acao == 3:
            todas_as_tarefas()
        elif acao == 4:
            tarefas_perdidas()
        elif acao == 5:
            adicionar_tarefas()
        elif acao == 6:
            deletar_tarefa()
        elif acao == 0:
            print("Bye!")
            exit()
        print("1) Today's tasks")
        print("2) Week's tasks")
        print("3) All tasks")
        print("4) Missed tasks")
        print("5) Add task")
        print("6) Delete task")
        print("0) Exit")
        acao = int(input())


Base.metadata.create_all(engine)
menu()
