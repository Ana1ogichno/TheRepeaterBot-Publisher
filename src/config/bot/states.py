from aiogram.fsm.state import StatesGroup, State


class States(StatesGroup):
    START = State()
    MAIN = State()
    VIEW_POSTS = State()
    EDIT_POSTS = State()
    FINISH = State()
