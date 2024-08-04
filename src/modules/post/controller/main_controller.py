from aiogram import Router
from .view import router as view_router
from .edit import router as edit_router

router = Router()
router.include_router(view_router)
router.include_router(edit_router)
