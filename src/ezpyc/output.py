from enum import Enum

class OutputType(Enum):
    HEADER = 1
    INFO = 2

def output(text: str, output_type: OutputType = OutputType.INFO) -> None:
    if(output_type == OutputType.HEADER):
        print('▒ {0}'.format(text))
    else:
        print('└─ {0}'.format(text))

__all__ = ['output', 'OutputType']