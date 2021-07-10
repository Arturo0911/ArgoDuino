from typing import Any, Union
from serial import Serial


class Arduino:
    """Arduino connection"""

    def __init__(self):
        self.port = "COM4"
        self.baudrate = 9600
        self.timeout = 2

    def _connection(self) -> Any:
        serial_conn = Serial(port=self.port,
                                    baudrate=self.baudrate,
                                    timeout=self.timeout)
        return serial_conn

    def read_lines(self, readers=20) -> Union[dict, list]:
        conn = self._connection()
        stack_data = list()
        object_data = dict()
        counter = 1
        while readers > 1:
            data = conn.readline().decode("ascii", errors="replace")
            stack_data.append(data)
            object_data[counter] = data
            counter += 1
            readers -= 1
        return object_data, stack_data
