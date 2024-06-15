import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from shapely.geometry import box
from shapely.affinity import rotate

def rotate_bbox_shapely(bbox, angle, origin):
    return rotate(bbox, angle, origin=origin, use_radians=False)

def calculate_iou(box1, box2):
    intersection = box1.intersection(box2).area
    union = box1.union(box2).area
    return intersection / union

def plot_bbox(ax, bbox, color, text=None):
    ax.plot(*bbox.exterior.xy, color=color)
    if text:
        x, y = bbox.exterior.xy
        ax.text(x[0], y[0], text, color='white', fontsize=10, ha='right', va='bottom', fontweight='bold')

def process_scene(scene_id, gt_labels, pred_labels, output_folder):
    bev = cv2.imread(os.path.join(bev_path, f"{scene_id}.png"))

    fig, ax = plt.subplots(figsize=(13, 13))
    ax.imshow(bev[:, :, [2, 1, 0]])

    true_positives, false_positives, false_negatives = 0, 0, 0

    for gt_label in gt_labels:
        class_label, x, y, w, l, im, re = gt_label
        gt_bbox = box(x - w / 2, y - l / 2, x + w / 2, y + l / 2)
        rotated_gt_bbox = rotate_bbox_shapely(gt_bbox, np.degrees(np.arctan2(im, re)), (x, y))

        max_iou = 0
        for pred_label in pred_labels:
            pred_x, pred_y, pred_w, pred_l, pred_im, pred_re, _, _, _ = pred_label
            pred_bbox = box(pred_x - pred_w / 2, pred_y - pred_l / 2, pred_x + pred_w / 2, pred_y + pred_l / 2)
            rotated_pred_bbox = rotate_bbox_shapely(pred_bbox, np.degrees(np.arctan2(pred_im, pred_re)), (pred_x, pred_y))

            iou = calculate_iou(rotated_gt_bbox, rotated_pred_bbox)
            max_iou = max(max_iou, iou)

        if max_iou > 0.5:
            plot_bbox(ax, rotated_gt_bbox, 'green', f"{max_iou:.2f}")
            true_positives += 1
        else:
            false_negatives += 1

    for pred_label in pred_labels:
        x, y, w, l, im, re, _, _, _ = pred_label
        pred_bbox = box(x - w / 2, y - l / 2, x + w / 2, y + l / 2)
        rotated_pred_bbox = rotate_bbox_shapely(pred_bbox, np.degrees(np.arctan2(im, re)), (x, y))
        plot_bbox(ax, rotated_pred_bbox, 'red')

    false_positives = len(pred_labels) - true_positives
    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)

    # Display precision and recall in the title
    title = f"Scene {scene_id}: Precision = {precision:.3f}, Recall = {recall:.3f}"
    plt.title(title, color='black', fontsize=14, fontweight='bold')
    
    plt.imshow(bev[:,:,[2,1,0]])
    # Save the image to the output folder
    output_path = os.path.join(output_folder, f"{scene_id}_output.png")
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()

# Base path
base_path = r"C:\Users\jdhru\OneDrive\Desktop\KITTI_Selection\KITTI_Selection"

# Subdirectories
bev_path = os.path.join(base_path, "bev")
labels_path = os.path.join(base_path, "labels")
predictions_path = os.path.join(base_path, "predictions")
output_images_path = os.path.join(base_path, "output_images")

# List of scene IDs
idxs = ['006067', '006059', '006310', '006227', '006121', '006315', '006211',
        '006042', '006130', '006374', '006037', '006097', '006048', '006206',
        '006253', '006098', '006291', '006312', '006329', '006054']

# Create a folder to save output images
os.makedirs(output_images_path, exist_ok=True)

# Loop over scene IDs
for scene_id in idxs:
    gt_labels = np.loadtxt(os.path.join(labels_path, f"{scene_id}.csv"), delimiter=",")
    pred_file_path = os.path.join(predictions_path, f"{scene_id}.csv")

    if os.path.getsize(pred_file_path) == 0:
        print(f"Scene {scene_id}: No predictions available (empty file).")
    else:
        pred_labels = np.loadtxt(pred_file_path, delimiter=",")
        process_scene(scene_id, gt_labels, pred_labels, output_images_path)

print("Output images saved in the folder:", output_images_path)