import argparse

from predictor import DepthEstimationModel


def main():
    parser = argparse.ArgumentParser(description="Depth estimation using ZoeDepth.")
    parser.add_argument("input_image", help="Path to input image.")
    parser.add_argument("output_image", help="Path to output depth map.")
    args = parser.parse_args()

    model = DepthEstimationModel()
    result = model.calculate_depthmap(args.input_image, args.output_image)
    print(result)


if __name__ == "__main__":
    main()
