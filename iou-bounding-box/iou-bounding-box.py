"""
 *     author:  _Shinomiyaa_
 *     created: 21.04.2026 18:48:12
"""
def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    x_left = max(box_a[0], box_b[0])
    y_top = max(box_a[1], box_b[1])
    x_right = min(box_a[2], box_b[2])
    y_bottom = min(box_a[3], box_b[3])
    
    # No overlap
    if x_right < x_left or y_bottom < y_top: return 0.0
    
    intersection_area = (x_right - x_left) * (y_bottom - y_top)
    
    area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])
    
    union_area = area_a + area_b - intersection_area
    
    return intersection_area / union_area
    
    pass