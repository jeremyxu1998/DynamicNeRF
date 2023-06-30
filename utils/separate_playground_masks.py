import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

separate_points_1 = np.array([[620, 280],
                            [678, 267],
                            [706, 303],
                            [731, 278],
                            [772, 305],
                            [809, 337],
                            [739, 342]])  # pixel locations

# for img_id in range(7):
#     I = np.asarray(PIL.Image.open('../data/Playground/motion_masks/00{}.png'.format(img_id)))
#     M0 = np.logical_not(I // 255).astype(int) * 255
#     plt.imsave('../data/Playground/motion_masks_0/00{}.png'.format(img_id), M0, cmap='gray')
#     M1 = np.copy(I)
#     M2 = np.copy(I)
#     # print(I.max(), I.min())
#     # print(I[0, 0], I[0, -1], I[-1, 0])
#     b = separate_points_1[img_id, 1] - separate_points_1[img_id, 0]
#     for i in range(I.shape[0]):
#         for j in range(I.shape[1]):
#             if (I[i, j] == 255) and (i-j < b):  # ballon
#                 M1[i, j] = 0
#             else:  # human
#                 M2[i, j] = 0
#     plt.imsave('../data/Playground/motion_masks_1/00{}.png'.format(img_id), M1, cmap='gray')
#     plt.imsave('../data/Playground/motion_masks_2/00{}.png'.format(img_id), M2, cmap='gray')
#     # plt.imshow(I)
#     # plt.show()

separate_points_2 = np.array([[[636, 275], [660, 311]],
                              [[638, 311], [659, 388]],
                              [[592, 261], [638, 346]],
                              [[570, 232], [626, 336]],
                              [[533, 251], [590, 365]]
                              ])
separate_ys_2 = np.array([255, 270, 247, 224, 238])  # above this, balloon

for img_id in range(7, 12):
    I = np.asarray(PIL.Image.open('../data/Playground/motion_masks/0{}.png'.format(str(img_id).zfill(2))))
    M0 = np.logical_not(I // 255).astype(int) * 255
    plt.imsave('../data/Playground/motion_masks_0/0{}.png'.format(str(img_id).zfill(2)), M0, cmap='gray')
    M1 = np.copy(I)
    M2 = np.copy(I)
    k = (separate_points_2[img_id-7, 1, 1] - separate_points_2[img_id-7, 0, 1]) / (separate_points_2[img_id-7, 1, 0] - separate_points_2[img_id-7, 0, 0])
    b = separate_points_2[img_id-7, 0, 1] - k * separate_points_2[img_id-7, 0, 0]
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            if (I[i, j] == 255):
                if i < separate_ys_2[img_id-7] or (i - k * j - b < 0):  # ballon
                    M1[i, j] = 0
                else:  # human
                    M2[i, j] = 0
    plt.imsave('../data/Playground/motion_masks_1/0{}.png'.format(str(img_id).zfill(2)), M1, cmap='gray')
    plt.imsave('../data/Playground/motion_masks_2/0{}.png'.format(str(img_id).zfill(2)), M2, cmap='gray')
