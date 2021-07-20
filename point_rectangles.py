from pynput.mouse import Controller

class Point_Rectangles:
    """This class allows to point and get the coordenates of corner of rectangles pointed by the mouse on the screen.
    """

    #region <Variables>

    _capture_started = False
    _origin_point = (0, 0)
    _current_position = (0, 0)

    _rectangle_coordenates = []

    _rectangles_to_capture = int
    _rectangles_registered = int
    _rectangle_corner_count = int

    mouse_ctrl = None

    #endregion

    #region <Attributes>



    #endregion

    #region <Constructor>

    def __init__(self, rectangles_to_capture: int):
        self._print_instruction()

        global mouse_ctrl
        mouse_ctrl = Controller()
        
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
        if self._capture_started == True and self._rectangles_registered != self._rectangles_to_capture:
            self._rectangle_coordenates.append(coordenate)

            self._rectangle_corner_count += 1

            if self._rectangle_corner_count > 3:
                self._rectangles_registered += 1
                self._rectangle_corner_count = 0
        else:
            self._capture_started = False

    #enderegion

    #region <Public Methods>

    def capture_corners(self):
        while True:
            cmd = input("> Command: ")

            if cmd == "-s" or cmd == "--start":
                self._capture_started = True
                
                print("> Capture started...")

            if (cmd == "-f" or cmd == "--finish") and self._capture_started == True:
                self._capture_started = False
                
                print("> Capture finished...")
            
            if (cmd == "-o" or cmd == "--origin") and self._capture_started == True:
                self._origin_point = mouse_ctrl.position
                
                print(f"> New origin setted: {self._origin_point} => (0, 0)")
            
            if cmd == "" and self._capture_started == True:
                self._current_position = tuple(map(lambda current_pos, origin: current_pos - origin, mouse_ctrl.position, self._origin_point))
                
                self._add_corner(self._current_position)

                print(f"> New corner point added: {self._current_position} relative to origin ({self._origin_point}) {self._rectangles_registered} / {self._rectangles_to_capture}")
            
            if (cmd == "-q" or cmd == "--quit"):
                # TODO: Crear una funcion que limpie todos los elementos y devuelva un array de ceros

                print("Exiting the rectangle capture, nothig has been saved")
                break

    #endregion