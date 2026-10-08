"""Re-render every data-driven SVG. The portrait is separate (prep_photo.py + make_ascii_svg.py)."""
import render_header_svg
import render_heatmap_svg
import render_info_card
import render_skyline_svg

for mod in (render_header_svg, render_info_card, render_skyline_svg, render_heatmap_svg):
    mod.main()
