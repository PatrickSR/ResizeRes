import os.path
import sys
from PIL import Image
#
# 在csdn无意看到的
# 原作者:版权声明：本文为博主原创文章，转载请保留出处http://blog.csdn.net/offbye
#
# ----------------------------------------------------------------------------
#
# 原作者是用Python2.x来运行的,然后我改了3.x,因为在我的电脑通常拿py3.5来运行的
# 开始要装PIL 这个module,作者也没提到
#
# 用法:python Resize.py [Project Path]/src/main/res
#


def image_resize(img_file, target, percent):
    """resize image and save to target path
    :param img_file: image file path
    :param target: save path
    :param percent: resize percent
    :return:
    """
    img = Image.open(img_file)
    print(img.size)
    width, height = img.size
    target_img = img.resize((int(width * percent), int(height * percent)), Image.ANTIALIAS)
    target_img.save(target)
    img.close()
    target_img.close()
    print(" save target image to " + target)


def path_resize(src, target, percent):
    if not os.path.isdir(src):
        print(src + " must be a dir")
        return -1

    os.chdir(src)
    cwd = os.getcwd()
    dirs = os.listdir(cwd)
    for file_name in dirs:
        print(file_name)
        if file_name.endswith('.9.png'):
            continue
        if file_name.endswith('.DS_Store'):
            continue

        src_file = os.path.join(cwd, file_name)

        if not os.path.exists(target):
            os.mkdir(target)
        image_resize(src_file, target + '/' + file_name, percent)


def android(res_dir):
    xxhdpi_path = res_dir + "/drawable-xxhdpi/"

    if not os.path.isdir(xxhdpi_path):
        print("xxhdpi_path must be a dir")
        return -1

    path_resize(xxhdpi_path, res_dir + '/drawable-xhdpi', 0.667)
    path_resize(xxhdpi_path, res_dir + '/drawable-hdpi', 0.444)
    path_resize(xxhdpi_path, res_dir + '/drawable-mdpi', 0.296)


if __name__ == "__main__":
    print('your android project res dir is :')
    print('=================================')

    try:
        if sys.argv[1]:
            print(sys.argv[1])
            android(sys.argv[1])
    except IndexError:
        print('you must input the android project res dir.')
