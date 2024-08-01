from aiogram.fsm.state import StatesGroup, State


class States(StatesGroup):
    START = State()
    MAIN = State()
    POSTS = State()
    FINISH = State()
