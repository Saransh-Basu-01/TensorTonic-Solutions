import math
def generate_anchors(feature_size: int, image_size: float, scales: list[float], aspect_ratios: list[float]) -> list[list[float]]:
    """
    Returns a list of [x1, y1, x2, y2] anchor boxes.
    """
    result=[]
    stride=image_size/feature_size
    for i in range(feature_size):
        for j in range(feature_size):
            cx=(j+0.5)*stride
            cy=(i+0.5)*stride
            for s in scales:
                for r in aspect_ratios:
                    w=s * math.sqrt(r)
                    h=s/(math.sqrt(r))
                    x1=cx-w/2
                    y1=cy-h/2
                    x2=cx+w/2
                    y2=cy+h/2
                    result.append([x1,y1,x2,y2])
    return result