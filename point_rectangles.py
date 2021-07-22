from pynput.mouse import Controller


class Point_Rectangles:
    """This class allows to point and get the coordenates of corner of rectangles pointed by the mouse on the screen.
    """

    #region <Variables>

    _EMPTY_NULL_ARRAY = [None, None, None, None]

    _capture_started = False
    _rectangles_captured = False
    _origin_point = (0, 0)
    _current_position = (0, 0)

    _rectangle_coordenates = []
    _rectangle_corners_coordinates = [None] * 4

    _rectangles_to_capture = int
    _rectangles_registered = int
    _rectangle_corner_count = int

    mouse_ctrl = None

    #endregion

    #region <Attributes>

    @property
    def get_last_rectangle_coordenates(self):
        """Retrieves the last four rectangle coordenates

        Returns:
            [list]: Last four coordenates of the last captured rectangle
        """
        if not self._rectangle_corners_coordinates:
            self._rectangle_corners_coordinates = self._EMPTY_NULL_ARRAY[:]

        return self._rectangle_corners_coordinates[:]

    @property
    def get_rectangles_coordenates(self):
        """Retrieves all the captured rectangles coordenates

        Returns:
            [list]: Coordinate lists
        """
        if not self._rectangle_coordenates:
            self._rectangle_coordenates = self._EMPTY_NULL_ARRAY[:]

        return self._rectangle_coordenates[:]

    @property
    def get_rectangles_registered(self):
        """Retrieves the number of rectangles registered

        Returns:
            [int]: Number of rectangles registered
        """
        return self._rectangles_registered

    #endregion

    #region <Constructor>

    def __init__(self, rectangles_to_capture: int):
        self._print_instruction()

        self.mouse_ctrl = Controller()
        
        self._rectangle_corner_count = 0
        self._rectangles_registered = 0
        self._rectangles_to_capture = rectangles_to_capture

    #endregion

    #region <Private Methods>

    def _print_instruction(self):
        print("""How to use: 
                1) Start the capture (-s)
                2) Position the mouse where the origin (0, 0) is going to be located
                3) Define an origin point (-o)
                4) Position the mouse at the firs point p0
                5) Press enter
                6) Position the mouse at the next point p1 and so on, like in the example shown below""")
        print("""Select the rectangle's corners in this way:
                p0---------------p1
                |                |
                |                |
                p3---------------p2 """)
        print("Use the following commands to capture the rectangle's corners:\n\t1) -s | --start\n\t2) -f | --finish\n\t3) -q | --quit\n\t4) -o | --origin\n\t5) -r | --restart\n\t6) Press \"enter\" to capture a corner\n\t")

    def _add_corner(self, coordenate):
        """Adds a new corner coordinate and increses the count of rectangles registerded once the 4 corners have been
        pointed

        Args:
            coordenate ([tupple]): Rectangle's corner coordinate
        """
        if self._capture_started and not self._rectangles_captured:
            # Asignación de nueva coordenada de esquina de rectangulo
            self._rectangle_corners_coordinates[self._rectangle_corner_count] = coordenate

            self._rectangle_corner_count += 1

            if self._rectangle_corner_count >= 4:
                self._rectangles_registered += 1
                self._rectangle_corner_count = 0

                # Se agrega self._rectangle_corners_coordinates[:] de esta forma debido a que si se hace directamente,
                # python copia la dirección del apuntador y al borrar la lista "_rectangle_corners_coordinates" tambien
                # lo hace la lista "_rectangle_coordenates"
                self._rectangle_coordenates.append(self._rectangle_corners_coordinates[:])

                if self._rectangles_registered == self._rectangles_to_capture: self._rectangles_captured = True
        
        elif self._capture_started and self._rectangles_captured:
            print(f"> Corner capture completed, no more corners were added...")

        else:
            print(f"> Corner capture not ready...")
            self._capture_started = False

    def _clean_array(self):
        """Cleans up all the arrays that were being filled
        """
        self._rectangle_corners_coordinates = []
        self._rectangle_coordenates = []

    #endregion

    #region <Public Methods>

    def capture_corners(self):
        """Initializes the rectangles' corners capture
        """
        while True:
            cmd = input("> Command: ")

            if cmd == "-s" or cmd == "--start":
                self._capture_started = True
                
                print("> Capture started...")

            if (cmd == "-f" or cmd == "--finish") and self._capture_started:
                self._capture_started = False
                
                print("> Capture finished...")
            
            if (cmd == "-o" or cmd == "--origin") and self._capture_started:
                self._origin_point = self.mouse_ctrl.position
                
                print(f"> New origin setted: {self._origin_point} => (0, 0)")
            
            if cmd == "" and self._capture_started and not self._rectangles_captured:
                self._current_position = list(tuple(map(lambda current_pos, origin: current_pos - origin, self.mouse_ctrl.position, self._origin_point)))
                
                self._add_corner(self._current_position)

                print(f"> New corner point added: {self._current_position} relative to origin ({self._origin_point})\n\tRectangles: {self._rectangles_registered} / {self._rectangles_to_capture}")

                # print(f"Corners: {self._rectangle_corners_coordinates}\nRectangle: {self._rectangle_coordenates}")
            
            if cmd == "" and self._capture_started and self._rectangles_captured:
                print(f"> Number of rectangles reached: {self._rectangles_registered} out of {self._rectangles_to_capture}")
                break
                
            if (cmd == "-q" or cmd == "--quit"):
                self._clean_array()

                print("Exiting the rectangle capture, nothig has been saved")
                break

    #endregion