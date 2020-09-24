import dicom2nifti
import dicom2nifti.settings as settings
import os
import shutil

#full_path = os.getcwd()
#print(full_path)

settings.disable_validate_orthogonal()
settings.enable_resampling()
settings.set_resample_spline_interpolation_order(1)
settings.set_resample_padding(-1000)
#settings.set_gdcmconv_path("D:/GDCM 3.0/bin")


dicom_directory = 'data/ct_scans/sampledicom_21'
output_folder = 'data/ct_scans/outputnii'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
else:
    shutil.rmtree(output_folder)
    os.makedirs(output_folder)

dicom2nifti.convert_directory(dicom_directory, output_folder)