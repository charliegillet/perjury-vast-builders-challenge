[Skip to content](https://supervision.roboflow.com/latest/detection/tools/polygon_zone/#supervision.detection.tools.polygon_zone.PolygonZone)

[Edit this page](https://github.com/roboflow/supervision/tree/main/docs/detection/tools/polygon_zone.md "Edit this page")

# Polygon Zone

## PolygonZone

## ```supervision.detection.tools.polygon_zone.PolygonZone` [¶](https://supervision.roboflow.com/latest/detection/tools/polygon_zone/\#supervision.detection.tools.polygon_zone.PolygonZone "Permanent link")

A class for defining a polygon-shaped zone within a frame for detecting objects.

Warning

PolygonZone uses the `tracker_id`. Read
[here](https://supervision.roboflow.com/latest/trackers/) to learn how to plug
tracking into your inference pipeline.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `polygon` |  | A polygon represented by a numpy array of shape<br>`(N, 2)`, containing the `x`, `y` coordinates of the points. |
| `triggering_anchors` |  | Any iterable of positions specifying<br>which anchors of the detections bounding box to consider when deciding on<br>whether the detection fits within the PolygonZone<br>(default: (sv.Position.BOTTOM\_CENTER,)). |
| `require_all_anchors` |  | If `True` (default), a detection is considered inside<br>the zone only when _every_ anchor in `triggering_anchors` is inside.<br>If `False`, the detection triggers as soon as _any_ anchor is inside.<br>Has no effect when `triggering_anchors` has a single entry.<br>This is anchor-based, not a true geometric box/polygon intersection<br>test: it fires only when a listed anchor point lands inside the mask.<br>Use mask/IoU-based approaches instead when full-overlap semantics are<br>required. |
| `current_count` |  | The current count of detected objects within the zone |
| `mask` |  | The 2D bool mask for the polygon zone |

Example

```
>>> import numpy as np
>>> import supervision as sv
>>> polygon = np.array([[100, 200], [200, 100], [300, 200], [200, 300]])
>>> polygon_zone = sv.PolygonZone(polygon=polygon)
>>> detections = sv.Detections(
...     xyxy=np.array([[180, 100, 220, 200], [400, 400, 450, 500]])
... )
>>> is_detections_in_zone = polygon_zone.trigger(detections)
>>> is_detections_in_zone
array([ True, False])
>>> polygon_zone.current_count
1
```

```
>>> polygon = np.array([[0, 0], [100, 0], [100, 100], [0, 100]])
>>> polygon_zone = sv.PolygonZone(
...     polygon=polygon,
...     triggering_anchors=[sv.Position.TOP_LEFT, sv.Position.BOTTOM_RIGHT],
...     require_all_anchors=False,
... )
>>> detections = sv.Detections(xyxy=np.array([[80, 80, 120, 120]]))
>>> polygon_zone.trigger(detections)
array([ True])
```

Source code in `src/supervision/detection/tools/polygon_zone.py`

|     |     |
| --- | --- |
| ```<br> 19<br> 20<br> 21<br> 22<br> 23<br> 24<br> 25<br> 26<br> 27<br> 28<br> 29<br> 30<br> 31<br> 32<br> 33<br> 34<br> 35<br> 36<br> 37<br> 38<br> 39<br> 40<br> 41<br> 42<br> 43<br> 44<br> 45<br> 46<br> 47<br> 48<br> 49<br> 50<br> 51<br> 52<br> 53<br> 54<br> 55<br> 56<br> 57<br> 58<br> 59<br> 60<br> 61<br> 62<br> 63<br> 64<br> 65<br> 66<br> 67<br> 68<br> 69<br> 70<br> 71<br> 72<br> 73<br> 74<br> 75<br> 76<br> 77<br> 78<br> 79<br> 80<br> 81<br> 82<br> 83<br> 84<br> 85<br> 86<br> 87<br> 88<br> 89<br> 90<br> 91<br> 92<br> 93<br> 94<br> 95<br> 96<br> 97<br> 98<br> 99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>109<br>110<br>111<br>112<br>113<br>114<br>115<br>116<br>117<br>118<br>119<br>120<br>121<br>122<br>123<br>124<br>125<br>126<br>127<br>128<br>129<br>130<br>131<br>132<br>133<br>134<br>135<br>136<br>137<br>138<br>139<br>140<br>141<br>142<br>143<br>144<br>145<br>146<br>147<br>148<br>149<br>150<br>151<br>152<br>153<br>154<br>155<br>156<br>157<br>158<br>159<br>160<br>161<br>162<br>163<br>``` | ````<br>class PolygonZone:<br>    """<br>    A class for defining a polygon-shaped zone within a frame for detecting objects.<br>    !!! warning<br>        PolygonZone uses the `tracker_id`. Read<br>        [here](/latest/trackers/) to learn how to plug<br>        tracking into your inference pipeline.<br>    Attributes:<br>        polygon: A polygon represented by a numpy array of shape<br>            `(N, 2)`, containing the `x`, `y` coordinates of the points.<br>        triggering_anchors: Any iterable of positions specifying<br>            which anchors of the detections bounding box to consider when deciding on<br>            whether the detection fits within the PolygonZone<br>            (default: (sv.Position.BOTTOM_CENTER,)).<br>        require_all_anchors: If `True` (default), a detection is considered inside<br>            the zone only when *every* anchor in `triggering_anchors` is inside.<br>            If `False`, the detection triggers as soon as *any* anchor is inside.<br>            Has no effect when `triggering_anchors` has a single entry.<br>            This is anchor-based, not a true geometric box/polygon intersection<br>            test: it fires only when a listed anchor point lands inside the mask.<br>            Use mask/IoU-based approaches instead when full-overlap semantics are<br>            required.<br>        current_count: The current count of detected objects within the zone<br>        mask: The 2D bool mask for the polygon zone<br>    Example:<br>        ```pycon<br>        >>> import numpy as np<br>        >>> import supervision as sv<br>        >>> polygon = np.array([[100, 200], [200, 100], [300, 200], [200, 300]])<br>        >>> polygon_zone = sv.PolygonZone(polygon=polygon)<br>        >>> detections = sv.Detections(<br>        ...     xyxy=np.array([[180, 100, 220, 200], [400, 400, 450, 500]])<br>        ... )<br>        >>> is_detections_in_zone = polygon_zone.trigger(detections)<br>        >>> is_detections_in_zone<br>        array([ True, False])<br>        >>> polygon_zone.current_count<br>        1<br>        ```<br>        ```pycon<br>        >>> polygon = np.array([[0, 0], [100, 0], [100, 100], [0, 100]])<br>        >>> polygon_zone = sv.PolygonZone(<br>        ...     polygon=polygon,<br>        ...     triggering_anchors=[sv.Position.TOP_LEFT, sv.Position.BOTTOM_RIGHT],<br>        ...     require_all_anchors=False,<br>        ... )<br>        >>> detections = sv.Detections(xyxy=np.array([[80, 80, 120, 120]]))<br>        >>> polygon_zone.trigger(detections)<br>        array([ True])<br>        ```<br>    """<br>    def __init__(<br>        self,<br>        polygon: npt.NDArray[np.int64],<br>        triggering_anchors: Iterable[Position] = (Position.BOTTOM_CENTER,),<br>        require_all_anchors: bool = True,<br>    ) -> None:<br>        """Build a zone from a polygon.<br>        Args:<br>            polygon: Zone boundary of shape `(N, 2)` holding the `x`, `y`<br>                coordinates of its vertices.<br>            triggering_anchors: Which anchors of a detection's bounding box<br>                decide whether it falls inside the zone.<br>            require_all_anchors: Whether every triggering anchor must be inside<br>                for the detection to count, rather than any one of them.<br>        Raises:<br>            ValueError: If `polygon` is not of shape `(N, 2)`, has fewer than<br>                `MIN_POLYGON_POINT_COUNT` vertices, or `triggering_anchors` is<br>                empty.<br>        """<br>        polygon = np.asarray(polygon)<br>        if polygon.ndim != 2 or polygon.shape[-1] != 2:<br>            raise ValueError(f"Polygon must have shape (N, 2); got {polygon.shape}.")<br>        # Fewer than three vertices enclose no area, so the mask below comes out<br>        # empty or a bare line and the zone silently never triggers. Reject it<br>        # here rather than let a zone that can never count look like a zone that<br>        # simply saw nothing. Zero vertices additionally breaks `np.max`.<br>        if len(polygon) < MIN_POLYGON_POINT_COUNT:<br>            raise ValueError(<br>                f"Polygon must have at least {MIN_POLYGON_POINT_COUNT} vertices "<br>                f"to enclose an area; got {len(polygon)}."<br>            )<br>        self.polygon = polygon.astype(int)<br>        # Materialize once so we can safely accept generators without exhausting them.<br>        self.triggering_anchors = list(triggering_anchors)<br>        if not self.triggering_anchors:<br>            raise ValueError("Triggering anchors cannot be empty.")<br>        self.require_all_anchors = require_all_anchors<br>        self.current_count = 0<br>        x_max, y_max = np.max(polygon, axis=0)<br>        self.mask = polygon_to_mask(<br>            polygon=polygon, resolution_wh=(x_max + 2, y_max + 2)<br>        )<br>    def trigger(self, detections: Detections) -> npt.NDArray[np.bool_]:<br>        """<br>        Determines if the detections are within the polygon zone.<br>        Anchor points are calculated from original (unclipped) detection boxes to<br>        avoid per-zone clipping shifting anchor positions. This prevents a single<br>        detection from being counted in multiple non-overlapping zones due to<br>        clipping artifacts, although overlapping zones may still legitimately<br>        contain the same detection.<br>        Args:<br>            detections: The detections to be checked against the polygon zone<br>        Returns:<br>            A boolean numpy array indicating<br>                if each detection is within the polygon zone<br>        """<br>        if len(detections) == 0:<br>            self.current_count = 0<br>            return cast(npt.NDArray[np.bool_], np.array([], dtype=bool))<br>        all_anchors = np.array(<br>            [<br>                np.rint(detections.get_anchors_coordinates(anchors)).astype(int)<br>                for anchors in self.triggering_anchors<br>            ]<br>        )<br>        mask_h, mask_w = self.mask.shape<br>        x, y = all_anchors[:, :, 0], all_anchors[:, :, 1]<br>        in_bounds = (x >= 0) & (y >= 0) & (x < mask_w) & (y < mask_h)<br>        x_safe = np.clip(x, 0, mask_w - 1)<br>        y_safe = np.clip(y, 0, mask_h - 1)<br>        anchor_hits = in_bounds & self.mask[y_safe, x_safe]<br>        reduce = np.all if self.require_all_anchors else np.any<br>        is_in_zone = reduce(anchor_hits, axis=0)<br>        self.current_count = int(np.sum(is_in_zone))<br>        return cast(npt.NDArray[np.bool_], is_in_zone.astype(bool))<br>```` |

### Methods: [¶](https://supervision.roboflow.com/latest/detection/tools/polygon_zone/\#supervision.detection.tools.polygon_zone.PolygonZone-functions "Permanent link")

#### ```__init__(polygon: npt.NDArray[np.int64], triggering_anchors: Iterable[Position] = (Position.BOTTOM_CENTER,), require_all_anchors: bool = True) -> None` [¶](https://supervision.roboflow.com/latest/detection/tools/polygon_zone/\#supervision.detection.tools.polygon_zone.PolygonZone.__init__ "Permanent link")

Build a zone from a polygon.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ##### `polygon` [¶](https://supervision.roboflow.com/latest/detection/tools/polygon_zone/\#supervision.detection.tools.polygon_zone.PolygonZone.__init__(polygon) "Permanent link") | `NDArray[int64]` | Zone boundary of shape `(N, 2)` holding the `x`, `y`<br>coordinates of its vertices. | _required_ |
| ##### `triggering_anchors` [¶](https://supervision.roboflow.com/latest/detection/tools/polygon_zone/\#supervision.detection.tools.polygon_zone.PolygonZone.__init__(triggering_anchors) "Permanent link") | `Iterable[Position]` | Which anchors of a detection's bounding box<br>decide whether it falls inside the zone. | `(BOTTOM_CENTER,)` |
| ##### `require_all_anchors` [¶](https://supervision.roboflow.com/latest/detection/tools/polygon_zone/\#supervision.detection.tools.polygon_zone.PolygonZone.__init__(require_all_anchors) "Permanent link") | `bool` | Whether every triggering anchor must be inside<br>for the detection to count, rather than any one of them. | `True` |

Raises:

| Type | Description |
| --- | --- |
| `ValueError` | If `polygon` is not of shape `(N, 2)`, has fewer than<br>`MIN_POLYGON_POINT_COUNT` vertices, or `triggering_anchors` is<br>empty. |

Source code in `src/supervision/detection/tools/polygon_zone.py`

|     |     |
| --- | --- |
| ```<br> 78<br> 79<br> 80<br> 81<br> 82<br> 83<br> 84<br> 85<br> 86<br> 87<br> 88<br> 89<br> 90<br> 91<br> 92<br> 93<br> 94<br> 95<br> 96<br> 97<br> 98<br> 99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>109<br>110<br>111<br>112<br>113<br>114<br>115<br>116<br>117<br>118<br>119<br>120<br>121<br>122<br>123<br>124<br>``` | ```<br>def __init__(<br>    self,<br>    polygon: npt.NDArray[np.int64],<br>    triggering_anchors: Iterable[Position] = (Position.BOTTOM_CENTER,),<br>    require_all_anchors: bool = True,<br>) -> None:<br>    """Build a zone from a polygon.<br>    Args:<br>        polygon: Zone boundary of shape `(N, 2)` holding the `x`, `y`<br>            coordinates of its vertices.<br>        triggering_anchors: Which anchors of a detection's bounding box<br>            decide whether it falls inside the zone.<br>        require_all_anchors: Whether every triggering anchor must be inside<br>            for the detection to count, rather than any one of them.<br>    Raises:<br>        ValueError: If `polygon` is not of shape `(N, 2)`, has fewer than<br>            `MIN_POLYGON_POINT_COUNT` vertices, or `triggering_anchors` is<br>            empty.<br>    """<br>    polygon = np.asarray(polygon)<br>    if polygon.ndim != 2 or polygon.shape[-1] != 2:<br>        raise ValueError(f"Polygon must have shape (N, 2); got {polygon.shape}.")<br>    # Fewer than three vertices enclose no area, so the mask below comes out<br>    # empty or a bare line and the zone silently never triggers. Reject it<br>    # here rather than let a zone that can never count look like a zone that<br>    # simply saw nothing. Zero vertices additionally breaks `np.max`.<br>    if len(polygon) < MIN_POLYGON_POINT_COUNT:<br>        raise ValueError(<br>            f"Polygon must have at least {MIN_POLYGON_POINT_COUNT} vertices "<br>            f"to enclose an area; got {len(polygon)}."<br>        )<br>    self.polygon = polygon.astype(int)<br>    # Materialize once so we can safely accept generators without exhausting them.<br>    self.triggering_anchors = list(triggering_anchors)<br>    if not self.triggering_anchors:<br>        raise ValueError("Triggering anchors cannot be empty.")<br>    self.require_all_anchors = require_all_anchors<br>    self.current_count = 0<br>    x_max, y_max = np.max(polygon, axis=0)<br>    self.mask = polygon_to_mask(<br>        polygon=polygon, resolution_wh=(x_max + 2, y_max + 2)<br>    )<br>``` |

#### ```trigger(detections: Detections) -> npt.NDArray[np.bool_]` [¶](https://supervision.roboflow.com/latest/detection/tools/polygon_zone/\#supervision.detection.tools.polygon_zone.PolygonZone.trigger "Permanent link")

Determines if the detections are within the polygon zone.

Anchor points are calculated from original (unclipped) detection boxes to
avoid per-zone clipping shifting anchor positions. This prevents a single
detection from being counted in multiple non-overlapping zones due to
clipping artifacts, although overlapping zones may still legitimately
contain the same detection.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ##### `detections` [¶](https://supervision.roboflow.com/latest/detection/tools/polygon_zone/\#supervision.detection.tools.polygon_zone.PolygonZone.trigger(detections) "Permanent link") | `Detections` | The detections to be checked against the polygon zone | _required_ |

Returns:

| Type | Description |
| --- | --- |
| `NDArray[bool_]` | A boolean numpy array indicating<br>if each detection is within the polygon zone |

Source code in `src/supervision/detection/tools/polygon_zone.py`

|     |     |
| --- | --- |
| ```<br>126<br>127<br>128<br>129<br>130<br>131<br>132<br>133<br>134<br>135<br>136<br>137<br>138<br>139<br>140<br>141<br>142<br>143<br>144<br>145<br>146<br>147<br>148<br>149<br>150<br>151<br>152<br>153<br>154<br>155<br>156<br>157<br>158<br>159<br>160<br>161<br>162<br>163<br>``` | ```<br>def trigger(self, detections: Detections) -> npt.NDArray[np.bool_]:<br>    """<br>    Determines if the detections are within the polygon zone.<br>    Anchor points are calculated from original (unclipped) detection boxes to<br>    avoid per-zone clipping shifting anchor positions. This prevents a single<br>    detection from being counted in multiple non-overlapping zones due to<br>    clipping artifacts, although overlapping zones may still legitimately<br>    contain the same detection.<br>    Args:<br>        detections: The detections to be checked against the polygon zone<br>    Returns:<br>        A boolean numpy array indicating<br>            if each detection is within the polygon zone<br>    """<br>    if len(detections) == 0:<br>        self.current_count = 0<br>        return cast(npt.NDArray[np.bool_], np.array([], dtype=bool))<br>    all_anchors = np.array(<br>        [<br>            np.rint(detections.get_anchors_coordinates(anchors)).astype(int)<br>            for anchors in self.triggering_anchors<br>        ]<br>    )<br>    mask_h, mask_w = self.mask.shape<br>    x, y = all_anchors[:, :, 0], all_anchors[:, :, 1]<br>    in_bounds = (x >= 0) & (y >= 0) & (x < mask_w) & (y < mask_h)<br>    x_safe = np.clip(x, 0, mask_w - 1)<br>    y_safe = np.clip(y, 0, mask_h - 1)<br>    anchor_hits = in_bounds & self.mask[y_safe, x_safe]<br>    reduce = np.all if self.require_all_anchors else np.any<br>    is_in_zone = reduce(anchor_hits, axis=0)<br>    self.current_count = int(np.sum(is_in_zone))<br>    return cast(npt.NDArray[np.bool_], is_in_zone.astype(bool))<br>``` |

## PolygonZoneAnnotator

## ```supervision.detection.tools.polygon_zone.PolygonZoneAnnotator` [¶](https://supervision.roboflow.com/latest/detection/tools/polygon_zone/\#supervision.detection.tools.polygon_zone.PolygonZoneAnnotator "Permanent link")

A class for annotating a polygon-shaped zone within a frame with a count of
detected objects.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `zone` |  | The polygon zone to be annotated |
| `color` |  | The color to draw the polygon lines, default is white |
| `thickness` |  | The thickness of the polygon lines, default is 2 |
| `text_color` |  | The color of the text on the polygon, default is black |
| `text_scale` |  | The scale of the text on the polygon, default is 0.5 |
| `text_thickness` |  | The thickness of the text on the polygon, default is 1 |
| `text_padding` |  | The padding around the text on the polygon, default is 10 |
| `font` |  | The font type for the text on the polygon,<br>default is cv2.FONT\_HERSHEY\_SIMPLEX |
| `center` |  | The center of the polygon for text placement |
| `display_in_zone_count` |  | Show the label of the zone or not. Default is True |
| `opacity` |  | The opacity of zone filling when drawn on the scene. Default is 0 |

Example

```
>>> import numpy as np
>>> import supervision as sv
>>> polygon = np.array([[100, 200], [200, 100], [300, 200], [200, 300]])
>>> polygon_zone = sv.PolygonZone(polygon=polygon)
>>> zone_annotator = sv.PolygonZoneAnnotator(zone=polygon_zone, thickness=2)
>>> scene = np.zeros((400, 400, 3), dtype=np.uint8)
>>> annotated_scene = zone_annotator.annotate(scene=scene)
>>> annotated_scene.shape
(400, 400, 3)
```

Source code in `src/supervision/detection/tools/polygon_zone.py`

|     |     |
| --- | --- |
| ```<br>166<br>167<br>168<br>169<br>170<br>171<br>172<br>173<br>174<br>175<br>176<br>177<br>178<br>179<br>180<br>181<br>182<br>183<br>184<br>185<br>186<br>187<br>188<br>189<br>190<br>191<br>192<br>193<br>194<br>195<br>196<br>197<br>198<br>199<br>200<br>201<br>202<br>203<br>204<br>205<br>206<br>207<br>208<br>209<br>210<br>211<br>212<br>213<br>214<br>215<br>216<br>217<br>218<br>219<br>220<br>221<br>222<br>223<br>224<br>225<br>226<br>227<br>228<br>229<br>230<br>231<br>232<br>233<br>234<br>235<br>236<br>237<br>238<br>239<br>240<br>241<br>242<br>243<br>244<br>245<br>246<br>247<br>248<br>249<br>250<br>251<br>252<br>253<br>254<br>255<br>256<br>257<br>258<br>259<br>260<br>261<br>262<br>263<br>264<br>265<br>266<br>267<br>268<br>269<br>270<br>271<br>272<br>``` | ````<br>class PolygonZoneAnnotator:<br>    """<br>    A class for annotating a polygon-shaped zone within a frame with a count of<br>    detected objects.<br>    Attributes:<br>        zone: The polygon zone to be annotated<br>        color: The color to draw the polygon lines, default is white<br>        thickness: The thickness of the polygon lines, default is 2<br>        text_color: The color of the text on the polygon, default is black<br>        text_scale: The scale of the text on the polygon, default is 0.5<br>        text_thickness: The thickness of the text on the polygon, default is 1<br>        text_padding: The padding around the text on the polygon, default is 10<br>        font: The font type for the text on the polygon,<br>            default is cv2.FONT_HERSHEY_SIMPLEX<br>        center: The center of the polygon for text placement<br>        display_in_zone_count: Show the label of the zone or not. Default is True<br>        opacity: The opacity of zone filling when drawn on the scene. Default is 0<br>    Example:<br>        ```pycon<br>        >>> import numpy as np<br>        >>> import supervision as sv<br>        >>> polygon = np.array([[100, 200], [200, 100], [300, 200], [200, 300]])<br>        >>> polygon_zone = sv.PolygonZone(polygon=polygon)<br>        >>> zone_annotator = sv.PolygonZoneAnnotator(zone=polygon_zone, thickness=2)<br>        >>> scene = np.zeros((400, 400, 3), dtype=np.uint8)<br>        >>> annotated_scene = zone_annotator.annotate(scene=scene)<br>        >>> annotated_scene.shape<br>        (400, 400, 3)<br>        ```<br>    """<br>    def __init__(<br>        self,<br>        zone: PolygonZone,<br>        color: Color = Color.WHITE,<br>        thickness: int = 2,<br>        text_color: Color = Color.BLACK,<br>        text_scale: float = 0.5,<br>        text_thickness: int = 1,<br>        text_padding: int = 10,<br>        display_in_zone_count: bool = True,<br>        opacity: float = 0,<br>    ) -> None:<br>        self.zone = zone<br>        self.color = color<br>        self.thickness = thickness<br>        self.text_color = text_color<br>        self.text_scale = text_scale<br>        self.text_thickness = text_thickness<br>        self.text_padding = text_padding<br>        self.font = cv2.FONT_HERSHEY_SIMPLEX<br>        self.center = get_polygon_center(polygon=zone.polygon)<br>        self.display_in_zone_count = display_in_zone_count<br>        self.opacity = opacity<br>    def annotate(<br>        self, scene: npt.NDArray[Any], label: str | None = None<br>    ) -> npt.NDArray[Any]:<br>        """<br>        Annotates the polygon zone within a frame with a count of detected objects.<br>        Args:<br>            scene: The image on which the polygon zone will be annotated<br>            label: A label for the count of detected objects<br>                within the polygon zone (default: None)<br>        Returns:<br>            The image with the polygon zone and count of detected objects<br>        """<br>        if self.opacity == 0:<br>            annotated_frame = draw_polygon(<br>                scene=scene,<br>                polygon=self.zone.polygon,<br>                color=self.color,<br>                thickness=self.thickness,<br>            )<br>        else:<br>            annotated_frame = draw_filled_polygon(<br>                scene=scene.copy(),<br>                polygon=self.zone.polygon,<br>                color=self.color,<br>                opacity=self.opacity,<br>            )<br>            annotated_frame = draw_polygon(<br>                scene=annotated_frame,<br>                polygon=self.zone.polygon,<br>                color=self.color,<br>                thickness=self.thickness,<br>            )<br>        if self.display_in_zone_count:<br>            annotated_frame = draw_text(<br>                scene=annotated_frame,<br>                text=str(self.zone.current_count) if label is None else label,<br>                text_anchor=self.center,<br>                background_color=self.color,<br>                text_color=self.text_color,<br>                text_scale=self.text_scale,<br>                text_thickness=self.text_thickness,<br>                text_padding=self.text_padding,<br>                text_font=self.font,<br>            )<br>        return cast(npt.NDArray[Any], annotated_frame)<br>```` |

### Methods: [¶](https://supervision.roboflow.com/latest/detection/tools/polygon_zone/\#supervision.detection.tools.polygon_zone.PolygonZoneAnnotator-functions "Permanent link")

#### ```annotate(scene: npt.NDArray[Any], label: str | None = None) -> npt.NDArray[Any]` [¶](https://supervision.roboflow.com/latest/detection/tools/polygon_zone/\#supervision.detection.tools.polygon_zone.PolygonZoneAnnotator.annotate "Permanent link")

Annotates the polygon zone within a frame with a count of detected objects.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ##### `scene` [¶](https://supervision.roboflow.com/latest/detection/tools/polygon_zone/\#supervision.detection.tools.polygon_zone.PolygonZoneAnnotator.annotate(scene) "Permanent link") | `NDArray[Any]` | The image on which the polygon zone will be annotated | _required_ |
| ##### `label` [¶](https://supervision.roboflow.com/latest/detection/tools/polygon_zone/\#supervision.detection.tools.polygon_zone.PolygonZoneAnnotator.annotate(label) "Permanent link") | `str | None` | A label for the count of detected objects<br>within the polygon zone (default: None) | `None` |

Returns:

| Type | Description |
| --- | --- |
| `NDArray[Any]` | The image with the polygon zone and count of detected objects |

Source code in `src/supervision/detection/tools/polygon_zone.py`

|     |     |
| --- | --- |
| ```<br>224<br>225<br>226<br>227<br>228<br>229<br>230<br>231<br>232<br>233<br>234<br>235<br>236<br>237<br>238<br>239<br>240<br>241<br>242<br>243<br>244<br>245<br>246<br>247<br>248<br>249<br>250<br>251<br>252<br>253<br>254<br>255<br>256<br>257<br>258<br>259<br>260<br>261<br>262<br>263<br>264<br>265<br>266<br>267<br>268<br>269<br>270<br>271<br>272<br>``` | ```<br>def annotate(<br>    self, scene: npt.NDArray[Any], label: str | None = None<br>) -> npt.NDArray[Any]:<br>    """<br>    Annotates the polygon zone within a frame with a count of detected objects.<br>    Args:<br>        scene: The image on which the polygon zone will be annotated<br>        label: A label for the count of detected objects<br>            within the polygon zone (default: None)<br>    Returns:<br>        The image with the polygon zone and count of detected objects<br>    """<br>    if self.opacity == 0:<br>        annotated_frame = draw_polygon(<br>            scene=scene,<br>            polygon=self.zone.polygon,<br>            color=self.color,<br>            thickness=self.thickness,<br>        )<br>    else:<br>        annotated_frame = draw_filled_polygon(<br>            scene=scene.copy(),<br>            polygon=self.zone.polygon,<br>            color=self.color,<br>            opacity=self.opacity,<br>        )<br>        annotated_frame = draw_polygon(<br>            scene=annotated_frame,<br>            polygon=self.zone.polygon,<br>            color=self.color,<br>            thickness=self.thickness,<br>        )<br>    if self.display_in_zone_count:<br>        annotated_frame = draw_text(<br>            scene=annotated_frame,<br>            text=str(self.zone.current_count) if label is None else label,<br>            text_anchor=self.center,<br>            background_color=self.color,<br>            text_color=self.text_color,<br>            text_scale=self.text_scale,<br>            text_thickness=self.text_thickness,<br>            text_padding=self.text_padding,<br>            text_font=self.font,<br>        )<br>    return cast(npt.NDArray[Any], annotated_frame)<br>``` |

## Comments

![Project Logo](https://media.roboflow.com/chat.png)

Ask AI

reCAPTCHA

Recaptcha requires verification.

protected by **reCAPTCHA**