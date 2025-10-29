import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

# Load a NIfTI file

nifti_img = nib.load('/Users/Mónica Monroy/Notas python/sub-01_task-rest_bold.nii.gz')

vol = nifti_img.get_fdata()


print(vol.shape)
print(type(vol))

vol50= vol[:,:,:,64]
print(vol50.shape)
'''
def gafvistas(vol=0,pos=0):
 volumen = 
 volx = vol[i]
 sagital = volx[pos[0], :, :]
 coronal= volx[:, pos[1], :]
 axial= volx[: , : , pos[2]]

 imgn = np.zeros((99,99))
 imgn[0:64,0:35] = sagital
 imgn[35:99,0:35] = coronal
 imgn[0:64,35:99] = axial

 plt.imshow(sagital)
 plt.imshow(coronal)
 plt.imshow(axial)
 plt.imshow(imgn)

 plt.show()

'''
sagital = vol50[45 , : , :]
coronal= vol50[: , 20 , :]
axial= vol50[: , : , 30]
axial=np.rot90(axial)

imgn = np.zeros((99,99))
imgn[0:64,0:35] = sagital
imgn[35:99,0:35] = coronal
imgn[0:64,35:99] = axial


print(sagital.shape)
print(coronal.shape)
print(axial.shape)

print(type(sagital))

plt.imshow(sagital)
plt.imshow(coronal)
plt.imshow(axial)
plt.imshow(imgn)

plt.show()


#gafvistas(vol50,[10,20,20]):



#sup izquierda 64*64



