from point_rectangles import Point_Rectangles
from config_json import Config_Json

def run():
    rectangle = Point_Rectangles(2)

    rectangle.capture_corners()

    print(f"Coordenadas de los rectangulos: {rectangle.get_rectangles_coordenates}")

    calibration = Config_Json(rectangle.get_rectangles_coordenates) #rectangle.get_rectangles_coordenates

    coordenates = calibration.get_calibration_coordenates()
    print(f"Calib saved: {coordenates}")

if __name__ == "__main__":
    run()