import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

# Load a NIfTI file

nifti_img = nib.load('sub-01_T1w.nii.gz')

vol = nifti_img.get_fdata()


print(vol.shape)
print(type(vol))

sagital = vol[100 , : , :]
coronal= vol[: , 100 , :]
axial= vol[: , : , 100]
axial=np.rot90(axial)

imgn = np.zeros((432,432))
imgn[0:256,0:256] = sagital
imgn[256:432,0:256] = coronal
imgn[0:256,256:432] = axial


print(sagital.shape)
print(coronal.shape)

print(type(sagital))

plt.imshow(sagital)
plt.imshow(coronal)
plt.imshow(axial)
plt.imshow(imgn)

plt.show()
