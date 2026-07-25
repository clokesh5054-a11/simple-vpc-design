import os
import sys

def get_svg_content():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 700" width="100%" height="100%">
  <defs>
    <!-- Arrow definitions -->
    <marker id="arrow-gray" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#4b5563" />
    </marker>
    <marker id="arrow-orange" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#ea580c" />
    </marker>
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#2563eb" />
    </marker>
    
    <!-- Soft shadow filter for modern UI feel -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
    <filter id="card-shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.05" />
    </filter>
  </defs>

  <style>
    .text-title { font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; font-weight: 700; font-size: 16px; }
    .text-body { font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; font-weight: 400; font-size: 12px; }
    .text-body-bold { font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; font-weight: 600; font-size: 12px; }
    .text-server { font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; font-weight: 700; font-size: 13px; fill: #ffffff; }
    .text-server-sub { font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; font-weight: 400; font-size: 11px; fill: #f1f5f9; }
    .text-server-tag { font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; font-weight: 600; font-size: 10px; fill: #ffedd5; }
  </style>

  <!-- Background -->
  <rect width="900" height="700" fill="#f8fafc" rx="16" />

  <!-- INTERNET -->
  <!-- Cloud Icon Drawing -->
  <path d="M 420 80 A 20 20 0 0 1 435 50 A 30 30 0 0 1 485 55 A 20 20 0 0 1 500 80 A 15 15 0 0 1 490 100 L 410 100 A 15 15 0 0 1 420 80 Z" 
        fill="#e0f2fe" stroke="#0284c7" stroke-width="2" filter="url(#shadow)" />
  <text x="450" y="88" class="text-body-bold" fill="#0369a1" text-anchor="middle">Internet</text>

  <!-- VPC CONTAINER -->
  <rect x="50" y="240" width="800" height="420" rx="12" fill="#ffffff" stroke="#f97316" stroke-width="2.5" stroke-dasharray="10 6" filter="url(#shadow)" />
  <text x="70" y="270" class="text-title" fill="#ea580c">AWS VPC (10.0.0.0/16)</text>

  <!-- INTERNET GATEWAY (IGW) -->
  <!-- Centered on the top boundary of VPC -->
  <circle cx="450" cy="240" r="26" fill="#fff7ed" stroke="#ea580c" stroke-width="2.5" filter="url(#card-shadow)" />
  <!-- Portal/Gateway Vector Icon -->
  <rect x="438" y="228" width="24" height="24" rx="4" fill="none" stroke="#ea580c" stroke-width="2" />
  <path d="M 450 224 L 450 256 M 436 240 L 464 240" stroke="#ea580c" stroke-width="2" />
  <text x="450" y="200" class="text-body-bold" fill="#ea580c" text-anchor="middle">Internet Gateway (IGW)</text>

  <!-- PUBLIC SUBNET -->
  <rect x="80" y="300" width="360" height="340" rx="8" fill="#f0f7ff" stroke="#2563eb" stroke-width="2" filter="url(#card-shadow)" />
  <text x="100" y="325" class="text-body-bold" fill="#1d4ed8">Public Subnet (10.0.1.0/24)</text>

  <!-- PRIVATE SUBNET -->
  <rect x="460" y="300" width="360" height="340" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2" filter="url(#card-shadow)" />
  <text x="480" y="325" class="text-body-bold" fill="#15803d">Private Subnet (10.0.2.0/24)</text>

  <!-- PUBLIC ROUTE TABLE -->
  <rect x="100" y="340" width="320" height="55" rx="6" fill="#fffbeb" stroke="#d97706" stroke-width="1.5" />
  <text x="115" y="360" class="text-body-bold" fill="#b45309">Public Route Table</text>
  <text x="115" y="380" class="text-body" fill="#78350f">Destination: 0.0.0.0/0 ➔ Target: IGW</text>

  <!-- SECURITY GROUP - WEB SERVER -->
  <rect x="100" y="415" width="320" height="205" rx="6" fill="#fafafa" stroke="#64748b" stroke-width="1.5" stroke-dasharray="6 4" />
  <text x="115" y="435" class="text-body-bold" fill="#334155">Security Group: Web Server SG</text>
  <text x="115" y="455" class="text-body" fill="#475569">• Ingress: SSH (Port 22) from User IP</text>
  <text x="115" y="472" class="text-body" fill="#475569">• Ingress: HTTP (Port 80) from Anywhere (0.0.0.0/0)</text>
  <text x="115" y="489" class="text-body" fill="#475569">• Ingress: HTTPS (Port 443) from Anywhere (0.0.0.0/0)</text>

  <!-- WEB EC2 INSTANCE -->
  <rect x="170" y="505" width="180" height="95" rx="8" fill="#f97316" stroke="#ea580c" stroke-width="2" filter="url(#shadow)" />
  <!-- Simple Stylized EC2 Icon Details -->
  <rect x="182" y="517" width="22" height="22" rx="4" fill="none" stroke="#ffffff" stroke-width="1.8" />
  <path d="M 188 528 L 198 528 M 193 523 L 193 533" stroke="#ffffff" stroke-width="1.5" />
  <text x="260" y="533" class="text-server" text-anchor="middle">EC2 Web Server</text>
  <text x="260" y="555" class="text-server-sub" text-anchor="middle">10.0.1.x (Public IP)</text>
  <text x="260" y="575" class="text-server-tag" text-anchor="middle">Amazon Linux 2023</text>

  <!-- SECURITY GROUP - APP SERVER -->
  <rect x="480" y="415" width="320" height="205" rx="6" fill="#fafafa" stroke="#64748b" stroke-width="1.5" stroke-dasharray="6 4" />
  <text x="495" y="435" class="text-body-bold" fill="#334155">Security Group: App Server SG</text>
  <text x="495" y="455" class="text-body" fill="#475569">• Ingress: TCP (All Ports) from Web SG</text>
  <text x="495" y="472" class="text-body" fill="#475569">• Ingress: Block all direct traffic from Internet</text>

  <!-- APP EC2 INSTANCE -->
  <rect x="550" y="505" width="180" height="95" rx="8" fill="#f97316" stroke="#ea580c" stroke-width="2" filter="url(#shadow)" />
  <!-- Simple Stylized EC2 Icon Details -->
  <rect x="562" y="517" width="22" height="22" rx="4" fill="none" stroke="#ffffff" stroke-width="1.8" />
  <path d="M 568 528 L 578 528 M 573 523 L 573 533" stroke="#ffffff" stroke-width="1.5" />
  <text x="640" y="533" class="text-server" text-anchor="middle">EC2 App Server</text>
  <text x="640" y="555" class="text-server-sub" text-anchor="middle">10.0.2.x (Private IP)</text>
  <text x="640" y="575" class="text-server-tag" text-anchor="middle">Amazon Linux 2023</text>

  <!-- CONNECTIVITY ARROWS -->

  <!-- Internet -> IGW -->
  <path d="M 450 105 L 450 206" stroke="#4b5563" stroke-width="2" fill="none" marker-end="url(#arrow-gray)" />
  <text x="460" y="145" class="text-body-bold" fill="#4b5563">User Access</text>

  <!-- IGW -> Public Route Table -->
  <path d="M 450 270 L 450 285 L 260 285 L 260 332" stroke="#ea580c" stroke-width="2" fill="none" marker-end="url(#arrow-orange)" />
  <text x="350" y="280" class="text-body-bold" fill="#ea580c">Route default (0.0.0.0/0)</text>

  <!-- Public RT -> Web Server SG / EC2 -->
  <path d="M 260 397 L 260 497" stroke="#2563eb" stroke-width="2" fill="none" marker-end="url(#arrow-blue)" />
  <text x="268" y="408" class="text-body-bold" fill="#2563eb">HTTP/HTTPS/SSH</text>

  <!-- Web Server -> App Server -->
  <path d="M 353 552 L 542 552" stroke="#2563eb" stroke-width="2.5" fill="none" marker-end="url(#arrow-blue)" />
  <text x="450" y="542" class="text-body-bold" fill="#2563eb" text-anchor="middle">TCP (Application Traffic)</text>

</svg>"""

def get_drawio_content():
    return """<mxfile host="65bd7114-4a7b-47e8-8b21-de6cd10e2b44" modified="2026-07-25T12:00:00.000Z" agent="Antigravity" version="21.6.8" type="device">
  <diagram id="vpc-design" name="Page-1">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- Internet (Cloud) -->
        <mxCell id="internet" value="Internet" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#e0f2fe;strokeColor=#0284c7;fontColor=#0369a1;fontStyle=1" vertex="1" parent="1">
          <mxGeometry x="390" y="30" width="120" height="70" as="geometry" />
        </mxCell>
        
        <!-- Internet Gateway (IGW) -->
        <mxCell id="igw" value="Internet Gateway&#xa;(IGW)" style="ellipse;shape=mxgraph.aws4.internet_gateway;whiteSpace=wrap;html=1;fillColor=#fff7ed;strokeColor=#ea580c;fontColor=#ea580c;fontStyle=1;verticalAlign=bottom;labelPosition=center;verticalLabelPosition=top" vertex="1" parent="1">
          <mxGeometry x="420" y="210" width="60" height="60" as="geometry" />
        </mxCell>
        
        <!-- VPC Container -->
        <mxCell id="vpc" value="AWS VPC (10.0.0.0/16)" style="rounded=1;arcSize=5;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#f97316;strokeWidth=2;dashed=1;fontColor=#ea580c;align=left;verticalAlign=top;spacingLeft=10;spacingTop=10;fontStyle=1" vertex="1" parent="1">
          <mxGeometry x="50" y="240" width="800" height="420" as="geometry" />
        </mxCell>
        
        <!-- Public Subnet -->
        <mxCell id="public_subnet" value="Public Subnet (10.0.1.0/24)" style="rounded=1;arcSize=5;whiteSpace=wrap;html=1;fillColor=#f0f7ff;strokeColor=#2563eb;strokeWidth=2;fontColor=#1d4ed8;align=left;verticalAlign=top;spacingLeft=10;spacingTop=10;fontStyle=1" vertex="1" parent="vpc">
          <mxGeometry x="30" y="60" width="360" height="340" as="geometry" />
        </mxCell>
        
        <!-- Private Subnet -->
        <mxCell id="private_subnet" value="Private Subnet (10.0.2.0/24)" style="rounded=1;arcSize=5;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#16a34a;strokeWidth=2;fontColor=#15803d;align=left;verticalAlign=top;spacingLeft=10;spacingTop=10;fontStyle=1" vertex="1" parent="vpc">
          <mxGeometry x="410" y="60" width="360" height="340" as="geometry" />
        </mxCell>

        <!-- Public Route Table -->
        <mxCell id="public_rt" value="Public Route Table&#xa;(0.0.0.0/0 -> IGW)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fffbeb;strokeColor=#d97706;fontColor=#b45309;fontStyle=1;fontSize=11" vertex="1" parent="public_subnet">
          <mxGeometry x="20" y="40" width="320" height="55" as="geometry" />
        </mxCell>

        <!-- Web SG -->
        <mxCell id="web_sg" value="Security Group: Web SG&#xa;(SSH: 22, HTTP: 80, HTTPS: 443)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fafafa;strokeColor=#64748b;dashed=1;fontColor=#334155;align=center;verticalAlign=top;spacingTop=5;fontSize=11" vertex="1" parent="public_subnet">
          <mxGeometry x="20" y="115" width="320" height="205" as="geometry" />
        </mxCell>

        <!-- Web EC2 Instance -->
        <mxCell id="web_ec2" value="EC2 Web Server&#xa;(Amazon Linux 2023)" style="shape=mxgraph.aws4.ec2;whiteSpace=wrap;html=1;fillColor=#f97316;strokeColor=#ea580c;fontColor=#ffffff;fontStyle=1;align=center;verticalAlign=bottom;labelPosition=center;verticalLabelPosition=top" vertex="1" parent="web_sg">
          <mxGeometry x="70" y="90" width="180" height="95" as="geometry" />
        </mxCell>

        <!-- App SG -->
        <mxCell id="app_sg" value="Security Group: App SG&#xa;(Traffic only from Web SG)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fafafa;strokeColor=#64748b;dashed=1;fontColor=#334155;align=center;verticalAlign=top;spacingTop=5;fontSize=11" vertex="1" parent="private_subnet">
          <mxGeometry x="20" y="115" width="320" height="205" as="geometry" />
        </mxCell>

        <!-- App EC2 Instance -->
        <mxCell id="app_ec2" value="EC2 App Server&#xa;(Amazon Linux 2023)" style="shape=mxgraph.aws4.ec2;whiteSpace=wrap;html=1;fillColor=#f97316;strokeColor=#ea580c;fontColor=#ffffff;fontStyle=1;align=center;verticalAlign=bottom;labelPosition=center;verticalLabelPosition=top" vertex="1" parent="app_sg">
          <mxGeometry x="70" y="90" width="180" height="95" as="geometry" />
        </mxCell>

        <!-- Connections/Arrows -->
        
        <!-- Internet -> IGW -->
        <mxCell id="edge1" value="User Access" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#4B5563;exitX=0.5;exitY=1;entryX=0.5;entryY=0;fontColor=#4B5563;fontStyle=1" edge="1" parent="1" source="internet" target="igw">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        
        <!-- IGW -> Public Route Table -->
        <mxCell id="edge2" value="Route default (0.0.0.0/0)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#ea580c;entryX=0.5;entryY=0;exitX=0.5;exitY=1;fontColor=#ea580c;fontStyle=1" edge="1" parent="1" source="igw" target="public_rt">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="450" y="270" as="sourcePoint" />
          </mxGeometry>
        </mxCell>

        <!-- Public RT -> Web Server -->
        <mxCell id="edge3" value="HTTP/HTTPS/SSH" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#2563eb;entryX=0.5;entryY=0;exitX=0.5;exitY=1;fontColor=#2563eb;fontStyle=1" edge="1" parent="1" source="public_rt" target="web_ec2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Web Server -> App Server -->
        <mxCell id="edge4" value="TCP (App Traffic)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2.5;strokeColor=#2563eb;exitX=1;exitY=0.5;entryX=0;entryY=0.5;fontColor=#2563eb;fontStyle=1" edge="1" parent="1" source="web_ec2" target="app_ec2">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="400" y="552" as="targetPoint" />
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""

def generate_png_diagram(output_path):
    from PIL import Image, ImageDraw, ImageFont

    # Create a 2x resolution canvas (1800x1400) for anti-aliasing, scaled down to 900x700
    scale = 2
    w, h = 900 * scale, 700 * scale
    image = Image.new("RGBA", (w, h), (248, 250, 252, 255)) # #f8fafc
    draw = ImageDraw.Draw(image)

    # Font handling
    font_names = ["segoeui.ttf", "arial.ttf", "calibri.ttf", "Helvetica", "DejaVuSans"]
    
    def get_font(size_px, bold=False):
        scaled_size = int(size_px * scale)
        font_name = "segoeuib.ttf" if bold else "segoeui.ttf"
        try:
            return ImageFont.truetype(font_name, scaled_size)
        except IOError:
            for fallback in font_names:
                try:
                    return ImageFont.truetype(fallback, scaled_size)
                except IOError:
                    pass
        return ImageFont.load_default()

    title_font = get_font(16, bold=True)
    body_bold_font = get_font(12, bold=True)
    body_font = get_font(12, bold=False)
    server_font = get_font(13, bold=True)
    server_sub_font = get_font(11, bold=False)
    server_tag_font = get_font(10, bold=True)

    # 1. VPC CONTAINER
    # Outer box
    vpc_box = [50 * scale, 240 * scale, 850 * scale, 660 * scale]
    # Draw dashed rectangle
    # Draw rounded rectangle with fill=white and border=orange
    draw.rounded_rectangle(vpc_box, radius=12*scale, fill=(255, 255, 255, 255), outline=(249, 115, 22, 255), width=int(2.5*scale))
    draw.text((70 * scale, 255 * scale), "AWS VPC (10.0.0.0/16)", fill=(234, 88, 12, 255), font=title_font)

    # 2. PUBLIC SUBNET
    pub_box = [80 * scale, 300 * scale, 440 * scale, 640 * scale]
    draw.rounded_rectangle(pub_box, radius=8*scale, fill=(240, 247, 255, 255), outline=(37, 99, 235, 255), width=2*scale)
    draw.text((100 * scale, 315 * scale), "Public Subnet (10.0.1.0/24)", fill=(29, 78, 216, 255), font=body_bold_font)

    # 3. PRIVATE SUBNET
    priv_box = [460 * scale, 300 * scale, 820 * scale, 640 * scale]
    draw.rounded_rectangle(priv_box, radius=8*scale, fill=(240, 253, 244, 255), outline=(22, 163, 74, 255), width=2*scale)
    draw.text((480 * scale, 315 * scale), "Private Subnet (10.0.2.0/24)", fill=(21, 128, 61, 255), font=body_bold_font)

    # 4. PUBLIC ROUTE TABLE
    rt_box = [100 * scale, 340 * scale, 420 * scale, 395 * scale]
    draw.rounded_rectangle(rt_box, radius=6*scale, fill=(255, 251, 235, 255), outline=(217, 119, 6, 255), width=int(1.5*scale))
    draw.text((115 * scale, 347 * scale), "Public Route Table", fill=(180, 83, 9, 255), font=body_bold_font)
    draw.text((115 * scale, 368 * scale), "Destination: 0.0.0.0/0 -> Target: IGW", fill=(120, 53, 15, 255), font=body_font)

    # 5. SECURITY GROUPS
    # Web SG
    web_sg_box = [100 * scale, 415 * scale, 420 * scale, 620 * scale]
    draw.rounded_rectangle(web_sg_box, radius=6*scale, fill=(250, 250, 250, 255), outline=(100, 116, 139, 255), width=int(1.5*scale))
    draw.text((115 * scale, 423 * scale), "Security Group: Web Server SG", fill=(51, 65, 85, 255), font=body_bold_font)
    draw.text((115 * scale, 445 * scale), "- Ingress: SSH (Port 22) from User IP", fill=(71, 85, 105, 255), font=body_font)
    draw.text((115 * scale, 465 * scale), "- Ingress: HTTP (Port 80) from Anywhere", fill=(71, 85, 105, 255), font=body_font)
    draw.text((115 * scale, 485 * scale), "- Ingress: HTTPS (Port 443) from Anywhere", fill=(71, 85, 105, 255), font=body_font)

    # App SG
    app_sg_box = [480 * scale, 415 * scale, 800 * scale, 620 * scale]
    draw.rounded_rectangle(app_sg_box, radius=6*scale, fill=(250, 250, 250, 255), outline=(100, 116, 139, 255), width=int(1.5*scale))
    draw.text((495 * scale, 423 * scale), "Security Group: App Server SG", fill=(51, 65, 85, 255), font=body_bold_font)
    draw.text((495 * scale, 445 * scale), "- Ingress: TCP (All Ports) from Web SG", fill=(71, 85, 105, 255), font=body_font)
    draw.text((495 * scale, 465 * scale), "- Ingress: Block direct traffic from Internet", fill=(71, 85, 105, 255), font=body_font)

    # 6. EC2 INSTANCES
    # Web EC2
    web_ec2_box = [170 * scale, 505 * scale, 350 * scale, 600 * scale]
    draw.rounded_rectangle(web_ec2_box, radius=8*scale, fill=(249, 115, 22, 255), outline=(234, 88, 12, 255), width=2*scale)
    # Simple EC2 icon: draw a small inner white square with border
    draw.rectangle([182*scale, 517*scale, 204*scale, 539*scale], fill=None, outline=(255, 255, 255, 255), width=int(1.8*scale))
    draw.line([188*scale, 528*scale, 198*scale, 528*scale], fill=(255, 255, 255, 255), width=int(1.5*scale))
    draw.line([193*scale, 523*scale, 193*scale, 533*scale], fill=(255, 255, 255, 255), width=int(1.5*scale))
    # Text
    draw.text((260 * scale, 520 * scale), "EC2 Web Server", fill=(255, 255, 255, 255), font=server_font, anchor="mt")
    draw.text((260 * scale, 545 * scale), "10.0.1.x (Public IP)", fill=(241, 245, 249, 255), font=server_sub_font, anchor="mt")
    draw.text((260 * scale, 568 * scale), "Amazon Linux 2023", fill=(255, 237, 213, 255), font=server_tag_font, anchor="mt")

    # App EC2
    app_ec2_box = [550 * scale, 505 * scale, 730 * scale, 600 * scale]
    draw.rounded_rectangle(app_ec2_box, radius=8*scale, fill=(249, 115, 22, 255), outline=(234, 88, 12, 255), width=2*scale)
    # Simple EC2 icon
    draw.rectangle([562*scale, 517*scale, 584*scale, 539*scale], fill=None, outline=(255, 255, 255, 255), width=int(1.8*scale))
    draw.line([568*scale, 528*scale, 578*scale, 528*scale], fill=(255, 255, 255, 255), width=int(1.5*scale))
    draw.line([573*scale, 523*scale, 573*scale, 533*scale], fill=(255, 255, 255, 255), width=int(1.5*scale))
    # Text
    draw.text((640 * scale, 520 * scale), "EC2 App Server", fill=(255, 255, 255, 255), font=server_font, anchor="mt")
    draw.text((640 * scale, 545 * scale), "10.0.2.x (Private IP)", fill=(241, 245, 249, 255), font=server_sub_font, anchor="mt")
    draw.text((640 * scale, 568 * scale), "Amazon Linux 2023", fill=(255, 237, 213, 255), font=server_tag_font, anchor="mt")

    # 7. INTERNET CLOUD
    # Draw cloud via overlapping circles/rectangles
    draw.ellipse([415*scale, 55*scale, 455*scale, 95*scale], fill=(224, 242, 254, 255), outline=(2, 132, 199, 255), width=2*scale)
    draw.ellipse([445*scale, 45*scale, 495*scale, 95*scale], fill=(224, 242, 254, 255), outline=(2, 132, 199, 255), width=2*scale)
    draw.ellipse([475*scale, 60*scale, 505*scale, 90*scale], fill=(224, 242, 254, 255), outline=(2, 132, 199, 255), width=2*scale)
    # Fill middle to cover borders
    draw.rectangle([430*scale, 65*scale, 490*scale, 90*scale], fill=(224, 242, 254, 255))
    draw.line([430*scale, 90*scale, 490*scale, 90*scale], fill=(224, 242, 254, 255), width=4*scale)
    draw.text((460 * scale, 68 * scale), "Internet", fill=(3, 105, 161, 255), font=body_bold_font, anchor="mt")

    # 8. INTERNET GATEWAY (IGW)
    draw.ellipse([424*scale, 214*scale, 476*scale, 266*scale], fill=(255, 247, 237, 255), outline=(234, 88, 12, 255), width=int(2.5*scale))
    draw.rectangle([438*scale, 228*scale, 462*scale, 252*scale], fill=None, outline=(234, 88, 12, 255), width=2*scale)
    draw.line([450*scale, 224*scale, 450*scale, 256*scale], fill=(234, 88, 12, 255), width=2*scale)
    draw.line([436*scale, 240*scale, 464*scale, 240*scale], fill=(234, 88, 12, 255), width=2*scale)
    draw.text((450 * scale, 193 * scale), "Internet Gateway (IGW)", fill=(234, 88, 12, 255), font=body_bold_font, anchor="mt")

    # 9. CONNECTIVITY ARROWS (using thick lines and simple polygonal arrowhead indicators)
    def draw_arrow(start, end, color=(75, 85, 99, 255), width=2*scale):
        # Draw line
        draw.line([start[0], start[1], end[0], end[1]], fill=color, width=width)
        # Simple arrowhead pointing down
        if start[0] == end[0]: # Vertical line
            if start[1] < end[1]: # Pointing down
                draw.polygon([end[0] - 6*scale, end[1] - 8*scale, end[0] + 6*scale, end[1] - 8*scale, end[0], end[1]], fill=color)
            else: # Pointing up
                draw.polygon([end[0] - 6*scale, end[1] + 8*scale, end[0] + 6*scale, end[1] + 8*scale, end[0], end[1]], fill=color)
        elif start[1] == end[1]: # Horizontal line
            if start[0] < end[0]: # Pointing right
                draw.polygon([end[0] - 8*scale, end[1] - 6*scale, end[0] - 8*scale, end[1] + 6*scale, end[0], end[1]], fill=color)
            else: # Pointing left
                draw.polygon([end[0] + 8*scale, end[1] - 6*scale, end[0] + 8*scale, end[1] + 6*scale, end[0], end[1]], fill=color)

    # Internet -> IGW
    draw_arrow((450*scale, 95*scale), (450*scale, 210*scale), color=(75, 85, 99, 255))
    draw.text((460*scale, 135*scale), "User Access", fill=(75, 85, 99, 255), font=body_bold_font)

    # IGW -> Route Table (orthogonal)
    draw.line([450*scale, 266*scale, 450*scale, 285*scale], fill=(234, 88, 12, 255), width=2*scale)
    draw.line([450*scale, 285*scale, 260*scale, 285*scale], fill=(234, 88, 12, 255), width=2*scale)
    draw_arrow((260*scale, 285*scale), (260*scale, 336*scale), color=(234, 88, 12, 255))
    draw.text((340*scale, 267*scale), "Route default (0.0.0.0/0)", fill=(234, 88, 12, 255), font=body_bold_font)

    # Route Table -> Web Server SG
    draw_arrow((260*scale, 395*scale), (260*scale, 501*scale), color=(37, 99, 235, 255))
    draw.text((268*scale, 402*scale), "HTTP/HTTPS/SSH", fill=(37, 99, 235, 255), font=body_bold_font)

    # Web Server -> App Server (horizontal arrow)
    draw_arrow((350*scale, 552*scale), (546*scale, 552*scale), color=(37, 99, 235, 255), width=int(2.5*scale))
    draw.text((448*scale, 532*scale), "TCP (App Traffic)", fill=(37, 99, 235, 255), font=body_bold_font, anchor="mt")

    # Downscale image using Lanczos filter for smooth anti-aliased edges
    resized_image = image.resize((900, 700), Image.Resampling.LANCZOS)
    resized_image.save(output_path, "PNG")
    print(f"Successfully rendered PNG diagram to {output_path}")

def main():
    workspace_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    # 1. Write SVG
    svg_path = os.path.join(workspace_dir, "architecture.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(get_svg_content())
    print(f"Wrote SVG to {svg_path}")

    # 2. Write Draw.io
    drawio_path = os.path.join(workspace_dir, "architecture.drawio")
    with open(drawio_path, "w", encoding="utf-8") as f:
        f.write(get_drawio_content())
    print(f"Wrote Draw.io to {drawio_path}")

    # 3. Create images directory and generate PNG
    images_dir = os.path.join(workspace_dir, "images")
    os.makedirs(images_dir, exist_ok=True)
    
    png_path_root = os.path.join(workspace_dir, "architecture.png")
    png_path_images = os.path.join(images_dir, "architecture.png")
    
    generate_png_diagram(png_path_root)
    
    # Copy PNG to images/
    import shutil
    shutil.copyfile(png_path_root, png_path_images)
    print(f"Copied PNG to {png_path_images}")

if __name__ == "__main__":
    main()
