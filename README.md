# Evaluation-of-an-object-detector-Complex-YOLO-
1 Goal

 The primary objective of the task is to assess the accuracy and performance of an object
 detection system, specifically the ComplexYOLO network, when applied to a subset of
 the KITTI dataset. The process involves converting 3D lidar point clouds into 2D bird’s
 eye view (BEV) images for ease of analysis and utilizing the trained network to detect
 objects in these images. The evaluation hinges on calculating the Intersection over Union
 (IoU) or Jaccard index between detected bounding boxes and ground truth, establishing
 a threshold to categorize detections as True Positives (TP), False Positives (FP), or False
 Negatives (FN).
 This assessment allows the determination of Precision and Recall metrics for each
 scene, providing insight into the detector’s ability to accurately identify objects within
 the dataset.
 
 2 Approach used
 
 The project’s approach methodically commenced with simplifying the intricate 3D lidar
 point cloud data from the KITTI dataset into 2D bird’s eye view (BEV) images, stream
lining the information for analysis. Employing the specialized ComplexYOLO network,
 facilitated the object detection process on these 2D BEV images. The subsequent evalua
tion involved measuring the consistency between the system’s detections and the ground
 truth by utilizing the Intersection over Union (IoU) metric. Establishing a threshold of
 0.5 for the IoU enabled the classification of detections into accurate (True Positives) or
 inaccurate (False Positives or False Negatives) categories.
 Precision and Recall metrics were calculated based on this threshold, providing in
sights into the system’s accuracy in correctly identifying objects and capturing all relevant
 instances within the dataset. The project emphasized transparent presentation, utilizing
 BEV images displaying both ground truth and detection boxes. Overall, this system
atic approach aimed to rigorously evaluate the ComplexYOLO network’s performance in
 object detection, yielding insights into its reliability and accuracy across various scenes
 within the dataset.
 Precision = TruePositives / (TruePositives + FalsePositives)
 Recall = True Positive/True Positive + False Negative
 IoU= Union Area/ Intersection Area

 ![006227_output (1)](https://github.com/RahmanFarhan555/Evaluation-of-an-object-detector-Complex-YOLO-/assets/170820777/2e606cbd-e5a0-4408-a761-9db1fcc3e2e5)
 ![006253_output (1)](https://github.com/RahmanFarhan555/Evaluation-of-an-object-detector-Complex-YOLO-/assets/170820777/62ccb0e6-05f7-4f95-bba1-2e45675d2810)
 ![006291_output (1)](https://github.com/RahmanFarhan555/Evaluation-of-an-object-detector-Complex-YOLO-/assets/170820777/3baa0272-4b69-45bc-97b8-629e560236ad)
 ![006310_output (1)](https://github.com/RahmanFarhan555/Evaluation-of-an-object-detector-Complex-YOLO-/assets/170820777/31e37939-6c21-4118-91be-05e4df26e902)
 ![006312_output (1)](https://github.com/RahmanFarhan555/Evaluation-of-an-object-detector-Complex-YOLO-/assets/170820777/e4a4fcf5-25a6-41ba-b450-edb974c06cba)
 ![006315_output (1)](https://github.com/RahmanFarhan555/Evaluation-of-an-object-detector-Complex-YOLO-/assets/170820777/d21549b9-f8df-404b-a101-2e41becb7e5a)
 ![006329_output (1)](https://github.com/RahmanFarhan555/Evaluation-of-an-object-detector-Complex-YOLO-/assets/170820777/d1b93a07-592a-4f49-96b4-9f7cc39cc2e4)
 ![006374_output (1)](https://github.com/RahmanFarhan555/Evaluation-of-an-object-detector-Complex-YOLO-/assets/170820777/5261b2f6-a6ca-4404-82d1-314dcaf128e5)
 ![006037_output (1)](https://github.com/RahmanFarhan555/Evaluation-of-an-object-detector-Complex-YOLO-/assets/170820777/8256b796-b117-431e-85f8-9eaf3ead170c)
 ![006042_output (1)](https://github.com/RahmanFarhan555/Evaluation-of-an-object-detector-Complex-YOLO-/assets/170820777/90724173-5f4f-4b19-a8f0-a6516673f219)
 ![006048_output (1)](https://github.com/RahmanFarhan555/Evaluation-of-an-object-detector-Complex-YOLO-/assets/170820777/f74a16f3-6819-4223-a8ad-a82158908e00)
 ![006054_output (1)](https://github.com/RahmanFarhan555/Evaluation-of-an-object-detector-Complex-YOLO-/assets/170820777/ce754627-b499-45cb-874f-651e158c90e3)
 ![006059_output (1)](https://github.com/RahmanFarhan555/Evaluation-of-an-object-detector-Complex-YOLO-/assets/170820777/ce29eb8d-0f7e-4ae1-a35d-e1c655ec2f24)
 ![006067_output (1)](https://github.com/RahmanFarhan555/Evaluation-of-an-object-detector-Complex-YOLO-/assets/170820777/18c087a8-673b-4c0b-a0bd-5d4d716df8e9)
 ![006097_output (1)](https://github.com/RahmanFarhan555/Evaluation-of-an-object-detector-Complex-YOLO-/assets/170820777/e0f8b6c5-bab2-48d4-8e31-2d91f352e8c1)
 ![006098_output (1)](https://github.com/RahmanFarhan555/Evaluation-of-an-object-detector-Complex-YOLO-/assets/170820777/6df431ef-e098-4fca-9b62-7102466c70f4)
 ![006121_output (1)](https://github.com/RahmanFarhan555/Evaluation-of-an-object-detector-Complex-YOLO-/assets/170820777/996c1572-ad21-4538-8c5e-87a969363d35)
 ![006130_output (1)](https://github.com/RahmanFarhan555/Evaluation-of-an-object-detector-Complex-YOLO-/assets/170820777/afbb9382-cd30-4ddd-912c-51a3f045b71b)
 ![006211_output (1)](https://github.com/RahmanFarhan555/Evaluation-of-an-object-detector-Complex-YOLO-/assets/170820777/75bfba43-202b-4089-bec6-e94031986a6a)


















