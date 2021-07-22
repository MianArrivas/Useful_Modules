import json, codecs

class Config_Json:
    """Permite guardar las configuraciones en formato JSON
    """

    #region <Variables>

    _EMPTY_NULL_ARRAY = [(0, 0), (0, 0), (0, 0), (0, 0)]
    _KEY_CALIBRATION_COORD = "calibration_coordenates"

    _calibration_coordenates = []
    _json_calibration_coordenates = {}
    
    #endregion

    #region <Attributes>

    @property
    def calibration_coordenates(self):
        """Retrieves the value coordenates

        Returns:
            [array]: It returns the saved coordinates in json file
        """
        if not self._calibration_coordenates:
            self._calibration_coordenates = self._EMPTY_NULL_ARRAY[:]
            self._json_calibration_coordenates = {self._KEY_CALIBRATION_COORD: self._calibration_coordenates}
        
        return self._calibration_coordenates[:], self._json_calibration_coordenates
    @calibration_coordenates.setter
    def calibration_coordenates(self, coordenates_to_save):
        """Sets and generates the json format of the coordenates

        Args:
            coordenates_to_save ([array]): Coordenates to be saved in a json format
        """
        if coordenates_to_save:
            self._calibration_coordenates = coordenates_to_save[:]
        else:
            self._calibration_coordenates = self._EMPTY_NULL_ARRAY

        self._json_calibration_coordenates = {self._KEY_CALIBRATION_COORD: self._calibration_coordenates}


    #endregion

    #region <Constructor>

    def __init__(self, calibration_coord=None):
        if calibration_coord is not None:
            self.calibration_coordenates = calibration_coord[:]
            # self._calibration_coordenates = calibration_coordenetaes[:]

            self.save_calibration()

    #endregion

    #region <Private Methods>

    

    #endregion

    #region <Public Methods>

    def save_calibration(self):
        """Saves the Json configuration coordinates as a calib.json file
        """
        with open('calib.json', 'wb') as config_file:
            # COnverts the json variable into a string for saving it
            json_str_calib = json.dumps(self._json_calibration_coordenates)

            json.dump(json_str_calib, codecs.getwriter('utf-8')(config_file), ensure_ascii=False)
            print(f"> JSON: {json_str_calib}")

    def get_calibration_coordenates(self, file_name='calib.json'):
        """Retrieves the calibrated coordenates saved in calib.json

        Args:
            file_name (str, optional): [Defines the calib file to read]. Defaults to 'calib.json'.

        Returns:
            [array]: Calibration coordenates saved in calibration file
        """
        with open(file_name) as config_file:
            self._json_calibration_coordenates = json.load(config_file)
            self._json_calibration_coordenates = json.loads(self._json_calibration_coordenates)

            self._calibration_coordenates = self._json_calibration_coordenates[self._KEY_CALIBRATION_COORD]
            
            return self._calibration_coordenates[:]


    #endregion