# Welcome to Code Kudos.
## Convert any image to sketch with Python

#### To see more like this Subscribe to 
##### Youtube: @codekudos
###### Instagram: @codekudos
####### Twitter: @code_kudos

import cv2
import matplotlib.pyplot as plt

img=cv2.imread('vj.jpeg')


RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert_img=cv2.bitwise_not(grey_img)
blur_img=cv2.GaussianBlur(invert_img, (277,277),0)
invblur_img=cv2.bitwise_not(blur_img)
sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)

rgb_sketch=cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(5,6))
rgb_sketch=cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_sketch)
plt.axis('off')
plt.savefig('output.png', dpi=300, bbox_inches='tight')
plt.show()