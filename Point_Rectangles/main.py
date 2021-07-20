from point_rectangles import Point_Rectangles

def run():
    rectangle = Point_Rectangles(5)

    rectangle.capture_corners()

    print(f"Coordenadas de los rectangulos: {rectangle.get_rectangles_coordenates}")


if __name__ == "__main__":
    run()