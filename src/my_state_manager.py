
class MyState:

    _init_func = None
    _loop_func = None
    _exit_func = None

class MyStateManager:

    def __init__(self, initial_state: MyState) -> None:
        # instance of MyState
        self._current_state = initial_state
        assert isinstance(self._current_state, MyState)
        self._state_step = 0    

    def run(self):
        
        pass
