from aiogram.fsm.state import StatesGroup, State


class States(StatesGroup):
    START = State()
    MAIN = State()
    VIEW_POST = State()
    EDIT_POST = State()
    FINISH = State()
