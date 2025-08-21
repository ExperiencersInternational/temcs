# Traffic England Motorway Camera Snapshots

A poorly coded Python tool (first time coding in Python) I made to download snapshots from motorway cameras in England every minute. No support for Traffic Wales, Traffic Scotland or TfL at this time.

> **Note:** This tool was made with assistance from Microsoft Copilot (I know it's not a good idea but I've never used Python). All images created from this tool are under Crown copyright, I am not affiliated with National Highways and there are no guarantees that you might get blocked from the website for using this tool. Please check that a camera feed is operational before downloading, this won't detect out of order cameras at this time. Tool requires the `requests` dependancy, will not run without it.
> **Important:** This must be ran through Command Prompt, it will not work through the Python app or double clicking the file (I don't know why and can't be bothered to solve it).

## How to use

1. Download the latest version of the script onto a computer (I'd recommend making a new folder for this tool).
2. Visit https://www.trafficengland.com/ and enable the layer for traffic cameras.
3. Find the camera you want to capture on the map and click on it. Make note of the camera ID.
4. Run the script through Command Prompt and insert the traffic camera ID.
5. Images will automatically be captured and saved into a Cameras folder every minute for your specified camera. Press Control+C to stop at any time.

## Examples

<img width="1615" height="617" alt="Image of a roundabout junction at night. The image is greyscale and you can see a few cars at the roundabout." src="https://github.com/user-attachments/assets/14c4a16d-b81c-41da-98fc-cb004cb11677" />
