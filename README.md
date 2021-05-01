				# PhotoScale
	### A simple Image cropping, resizing and mainly an image compression tool

### Intro:
	PhotoScale is a very simple gui based application built with python. It can help you to quickly crop your image,
change resolution of your image and compress your image. It can reduce file size remarkably keeping image quality.
It uses Python Imaging Library(PIL) to do that. It also has a simple graphical user interface built with python tkinter.

[Actually tried to have some fun with pillow and so tried to mix it with a gui using my noob coding:)]

### Basic Information:
Program window: 1000x650 (non-resizable)
File Size:- comressed - 13/14 mb, installed - 28 mb ( python and other packages combined)
[You can grab the .py script from github and install 'pillow' module if you already have python]
Supported Platforms: Windows (python script will work in linux and mac)
Performance:- RAM usage:20-30 mb ( CPU usage should be nothing at maximum time. But may use some while processing)

### How to use:
	Using it is very simple with its simple gui. First install this application through the installation wizard.
Open the PhotoScale.exe file. You can see some buttons and options there.
1. Open: Simply ask you to choose an image file from your storage drive. Just select any image file here.
2. Save: After adjusting the settings and processing use this to save your new image to a seperate directory.
	*** Giving file name with extension may result in increased file size without compression. So better to give the name only,
unless you need a specific format too much. Default format for saving is Jpg or the original one. (see the usage of jpg checkbox for more)
3. Documentation/Publishing page: This button just take you to the github publishing page. You can find all details of it there.
		https://github.com/UnknownComplexity/PhotoScale
#### Entry:
>> You will see the entry input boxes in the right side.

	***** Always hit enter after typing the value. Otherwise, the the value may not change.

##### Resolution:
Resoultion or size of the image is important fact to image file size and quality. Higher the resoulution better the quality
but larger the file size. And lower the res. smaller the file size but quality drops. So change res. as you need.

4. The first entry is for the target width in px and second one for height. The default value is 2*Original/3. 
	* Under this you will see the proportional button. It is checked by default. It keeps the ratio of orignal height and width same
	to your given input. That means if you give the value of width, height will be changed automatically and vice versa.
	Unchek this only if you want to stretch or change your image res. ratio.

5. Quality: Then you will find the quality option. It is the main thing behind compression. Smaller the value better the compression.
But it will generate poor quality image, if the value is too small. Default value is 85. You can play around with this and see which one is 
better for you. Range is 0-100.
   	[Note that png like RGBA output formats doesnt support these. Which may increase output size a lot as described in the jpg checkbox section.]
## Jpg checkbox: The best image format for compression is JPEG(.jpg etc) and mode is 'RGB'. On the otherhand .png, .tif, .bmp and etc are loseless 
image format. *** They can keep transparency as the mode may be "RGBA". But this is not ideal for image compression. So if you want to compress that kind of
images with PhotoScale, it will convert the image to "RGB" and .jpg when this checkbox is checked(checked by default). But you will lose the transparent 
area of your image if available. Here you need another checkbox **"White Background"**. Basically it fills the transparent area with complete white.
And if its not checked (checked by default) transparent areas will be filled by complete black. So use it as your need.
		[*If you enter any extension in save dialog, image compression may not work even though it is checked*]
#### Crop:
Here is the simple cropping properties. You can see some entry for value inputs as well as some sliders for easy adjustment. You can guess the 
cropped image by looking at the red rectangle in your image preview. 
	** The cropping values are actually executed on the original(or processed) size of the image. So while doing both resizing and cropping,
	   the resolution value will automatically change according to the cropping values keeping the ratio correct. Default crop values are 0.
Left: Number of pixels to crop from the left side.
Right: Number of pixels to crop from the right.
Top: Number of pixels to crop from the top.
Bottom: Number of pixels to crop from the bottom.

Process: Finally here is the process button. As you click on it, you can't go back to your previous image(PhotoScale will not affect your original image.
So you can always reopen the original image) but further change it more. After clicking on it you can see your new image in the preview(quality setting
is not applicable for the preview). Remember to save the new image after you are done processing.

Preview: When you open a new image, you will see a preview(max 800x600, else keep ratio) in the wide blank space.
Every time you process the image the condition will be updated. Besides you will see a red rectangle around your image which refers to the crop area.

Conclusion: You can find my code in github. My noob coding may not appear clear to everyone. Besides many bugs, inefficient parts can be found.
Please let me know that there.

		----------------THANKS FOR INSTALLING-----------------