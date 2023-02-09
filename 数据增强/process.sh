python addnoisy.py --src ../dataset/train/images --dst ../dataset/train/images_noise
cp -r ../dataset/train/labels ../dataset/train/labels_noise
python blur.py --src ../dataset/train/images --dst ../dataset/train/images_blur
cp -r ../dataset/train/labels ../dataset/train/labels_blur
python rgb2gray.py --src ../dataset/train/images --dst ../dataset/train/images_gray
cp -r ../dataset/train/labels ../dataset/train/labels_gray
