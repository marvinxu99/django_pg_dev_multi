# https://blog.jonasneubert.com/2019/01/23/barcode-generation-python/

# https://www.ghostscript.com/

# (1) pip install treepoem
#     it will install treepoem 3.3.1 and Pillow 7.0.0

# (2) Install ghostscript    - 32bit


# Another solution is to (1) edit the 
# C:\Users\Windows.UserName\AppData\Local\Programs\Python\Python37\Lib\site-packages\treepoem__init__.py
# the script is looking for gs.exe, change to gswin32.exe as shown below.
# (2) Then add the GhostScriptInstallDir\bin in the PATH in windows.

# def _get_ghostscript_binary():
#     binary = "gswin32c" # changed from 'gs' to 'gswin32c'

#     if sys.platform.startswith("win"):
#         binary = EpsImagePlugin.gs_windows_binary
#         if not binary:
#             raise TreepoemError(
#                 "Cannot determine path to ghostscript, is it installed?"
#             )

#     return binary

#

from django.shortcuts import render
#from django.utils import timezone
import datetime

import treepoem


def generate_barcode(text=None):
    data = text
    if text is not None:
        data = text
    else:
        data = 'Winter WinnPy'
    
    image = treepoem.generate_barcode(
        barcode_type='qrcode',
        data=data
        )

    # file_name = 'barcode_' + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + '.png'
    # image.convert('1').save(file_name)
    image.convert('1').save('barcode.png')


def barcode_req(request):
    barcode_types = ['QR Code', 'other code']    
    context = {
            'barcode_types': barcode_types,
        }
    return render(request, 'polls/barcode_req.html', context)


def barcode_disp(request):
        
    return render(request, 'polls/barcode_disp.html')


if __name__ == "__main__":
    generate_barcode()


