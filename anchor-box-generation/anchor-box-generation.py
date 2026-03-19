"""
 *     author:  Shinomiyaaa
 *     created: 19.03.2026 22:52:01
"""
def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    # Write code here
def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    anchors = []
    stride = image_size / feature_size

    for i in range(feature_size):
        for j in range(feature_size):
            center_x = (j + 0.5) * stride
            center_y = (i + 0.5) * stride
            for scale in scales:
                for aspect_ratio in aspect_ratios:
                    width = scale * (aspect_ratio ** 0.5)
                    height = scale / (aspect_ratio ** 0.5)

                    xmin = center_x - width / 2
                    ymin = center_y - height / 2
                    xmax = center_x + width / 2
                    ymax = center_y + height / 2
                    anchors.append([xmin, ymin, xmax, ymax])
    return anchors