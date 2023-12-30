
# Zoe Depth Estimation

A brief description of what this project does and who it's for


## Usage/Examples

### CLI Usage
```bash
usage: cli.py [-h] input_image output_image

Depth estimation using ZoeDepth.

positional arguments:
  input_image   Path to input image.
  output_image  Path to output depth map.

options:
  -h, --help    show this help message and exit
```
### API Usage

```
http://127.0.0.1:8000/predict
```

## Installation

Install depth estimation project with pip

```bash
pip install -r requirements.txt
```
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`


## Deployment

To deploy this project run

```bash
  npm run deploy
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

