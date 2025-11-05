import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

# -------------------------
# Cargar la imagen NIfTI
# -------------------------
nifti_img = nib.load('/Users/Mónica Monroy/Notas python/sub-01_task-rest_bold.nii.gz')
vol = nifti_img.get_fdata()
vol = vol[:, :, :, 0]  # si es 4D, tomamos el primer volumen

nx, ny, nz = vol.shape
ix, iy, iz = nx // 2, ny // 2, nz // 2  # cortes iniciales centrales

# -------------------------
# Crear figura y subplots
# -------------------------
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

# Dibujamos los cortes iniciales
axes[0].imshow(np.rot90(vol[ix, :, :]), cmap='gray')
axes[0].set_title('Sagital')
axes[1].imshow(np.rot90(vol[:, iy, :]), cmap='gray')
axes[1].set_title('Coronal')
axes[2].imshow(np.rot90(vol[:, :, iz]), cmap='gray')
axes[2].set_title('Axial')

# -------------------------
# Función de clic
# -------------------------
def onclick(event):
    global ix, iy, iz

    if event.inaxes == axes[0]:  # Sagital
        iy = int(event.xdata)
        iz = int(vol.shape[2] - event.ydata)
    elif event.inaxes == axes[1]:  # Coronal
        ix = int(event.xdata)
        iz = int(vol.shape[2] - event.ydata)
    elif event.inaxes == axes[2]:  # Axial
        ix = int(event.xdata)
        iy = int(event.ydata)

    # Limpiar y dibujar de nuevo
    for ax in axes:
        ax.clear()

    axes[0].imshow(np.rot90(vol[ix, :, :]), cmap='gray')
    axes[0].set_title('Sagital')
    axes[1].imshow(np.rot90(vol[:, iy, :]), cmap='gray')
    axes[1].set_title('Coronal')
    axes[2].imshow(np.rot90(vol[:, :, iz]), cmap='gray')
    axes[2].set_title('Axial')

    plt.draw()  # refrescar la figura

# -------------------------
# Conectar el evento de clic
# -------------------------
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()