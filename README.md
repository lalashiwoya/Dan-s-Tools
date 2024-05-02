## Tools Dan Will Use Today

1. **MP4toGIF Tool**
2. **MP4 Speed Change**
3. **Pdf Merge**

### Setup

To set up the environment for these tools, execute the following commands:

```bash
conda create -n tools python=3.11
conda activate tools
pip install -r requirements.txt
```
Ensure that [**ffmpeg**](https://ffmpeg.org/download.html) is successfully installed. After installation, write the path of ffmpeg <**FFMPEG**> to the `.env` file, using `env.example` as a template for reference.

### Usage
For guidance on how to use these tools, refer to the examples in `tool_usage.ipynb`.

### Testing
To verify that these tools are functioning correctly on your machine, execute the following command:
```bash
python -m pytest
```


