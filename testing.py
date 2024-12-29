import cv2
if cv2.ocl.haveOpenCL():
    cv2.ocl.setUseOpenCL(True)
    print("OpenCL is enabled for OpenCV.")
else:
    print("OpenCL is not supported or enabled on your system.")