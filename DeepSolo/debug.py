import inspect

def debug_print(msg):
    current_frame = inspect.currentframe()
    outer_frame = inspect.getouterframes(current_frame, 2)
    
    frame_info = outer_frame[1]
    
    function_name = frame_info.function
    module_name = inspect.getmodule(frame_info[0]).__name__
    
    print(f"[{module_name}.{function_name}]: {str(msg)}")