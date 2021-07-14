from typing import Any, Tuple, Dict
from serial import Serial


class Arduino:
    """Arduino connection"""

    def __init__(self):
        self.port = "COM4"
        self.baud_rate = 9600
        self.timeout = 2

    def _connection(self) -> Any:
        serial_conn = Serial(port=self.port,
            baudrate=self.baud_rate,
            timeout=self.timeout)
        return serial_conn

    def read_lines(self, readers=20) -> Tuple[Dict[int, Any], list]:
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
