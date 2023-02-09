import os

if __name__ == '__main__':
    classes = ['images', 'images_blur', 'images_gray', 'images_noise']
    
    if not os.path.exists('process'):
        os.mkdir('process')
        os.mkdir('process/train')
        os.mkdir('process/train/images')
        os.mkdir('process/train/labels')
        os.system('cp -r ../dataset/test process/')
        os.system('cp -r ../dataset/val process/')
    
    image_path = 'process/train/images'
    label_path = 'process/train/labels'
    
    num = 1
    for cls in classes:
        path = os.path.join('../dataset/train', cls)
        images = os.listdir(path)
        
        for x in images:
            name  = x.replace('.jpg', '')
            image = name + '.jpg'
            label = name + '.txt'
            
            src_image_path = os.path.join('../dataset/train', cls)
            src_image_path = os.path.join(src_image_path, image)
            src_label_path = os.path.join('../dataset/train', cls.replace('images', 'labels'))
            src_label_path = os.path.join(src_label_path, label)
            
            os.system('cp {} {}/image_{:06d}.jpg'.format(src_image_path, image_path, num))
            os.system('cp {} {}/image_{:06d}.txt'.format(src_label_path, label_path, num))
            num += 1
