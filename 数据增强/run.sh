python generateblur.py --src data-non/images_blur --dst data-non/images_blur_gb
python generateocr.py  --src data-non/images_blur --dst data-non/images_blur_gc1
python generateocr2.py --src data-non/images_blur --dst data-non/images_blur_gc2
python generateocr3.py --src data-non/images_blur --dst data-non/images_blur_gc3
python generateblur.py --src data-non/images_gray --dst data-non/images_gray_gb
python generateocr.py  --src data-non/images_gray --dst data-non/images_gray_gc1
python generateocr2.py --src data-non/images_gray --dst data-non/images_gray_gc2
python generateocr3.py --src data-non/images_gray --dst data-non/images_gray_gc3
python generateblur.py --src data-non/images_noise --dst data-non/images_noise_gb
python generateocr.py  --src data-non/images_noise --dst data-non/images_noise_gc1
python generateocr2.py --src data-non/images_noise --dst data-non/images_noise_gc2
python generateocr3.py --src data-non/images_noise --dst data-non/images_noise_gc3
