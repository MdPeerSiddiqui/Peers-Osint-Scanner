"""
Generate Executive PDF Report for Day 1 Deliverable
Sqrock IT Solution — Alpha 2 Internship (Cybersecurity Track)
Author: Md Peer Siddiqui
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable, PageBreak
)

def create_report(output_pdf_path="reports/Day01_OSINT_Report_Sqrock_MdPeerSiddiqui.pdf"):
    os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)
    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    
    # Custom palette
    primary_color = colors.HexColor("#0f172a")     # Dark slate
    accent_color = colors.HexColor("#0284c7")      # Cyber blue
    bg_light = colors.HexColor("#f8fafc")
    text_dark = colors.HexColor("#1e293b")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=primary_color,
        spaceAfter=3
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=accent_color,
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15,
        textColor=primary_color,
        spaceBefore=8,
        spaceAfter=5
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=text_dark,
        spaceAfter=4
    )

    meta_label = ParagraphStyle(
        'MetaLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=primary_color
    )

    meta_val = ParagraphStyle(
        'MetaVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=text_dark
    )

    story = []

    # 1. Header Banner & Title
    story.append(Paragraph("CYBERSECURITY INTERNSHIP — PRACTICAL LAB REPORT", subtitle_style))
    story.append(Paragraph("DAY 01: Passive OSINT & Reconnaissance Tool", title_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=accent_color, spaceBefore=2, spaceAfter=8))

    # 2. Executive Metadata Grid
    meta_data = [
        [
            Paragraph("Intern Name:", meta_label), Paragraph("Md Peer Siddiqui", meta_val),
            Paragraph("Program:", meta_label), Paragraph("Alpha 2 — Cybersecurity Track", meta_val)
        ],
        [
            Paragraph("Issuing Body:", meta_label), Paragraph("Sqrock IT Solution", meta_val),
            Paragraph("Date of Execution:", meta_label), Paragraph("October 20, 2026", meta_val)
        ],
        [
            Paragraph("Target Domain:", meta_label), Paragraph("example.com (RFC 2606 Lab Target)", meta_val),
            Paragraph("Tool Developed:", meta_label), Paragraph("PEER'S OSINT Scanner v1.0", meta_val)
        ]
    ]

    meta_table = Table(meta_data, colWidths=[85, 185, 95, 175])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg_light),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 6))

    # 3. Objective & Value Addition Section
    story.append(Paragraph("1. Curriculum Scope vs. Extra Engineering Delivered", h2_style))
    scope_data = [
        [Paragraph("Sqrock Prescribed Minimum Requirements", meta_label), Paragraph("Extra Value & Engineering Implemented (PEER'S OSINT Scanner)", meta_label)],
        [
            Paragraph("• Build basic Python OSINT script<br/>• Resolve domain DNS and WHOIS info<br/>• Query IP Geolocation endpoint<br/>• Output screenshot & 1-page report", body_style),
            Paragraph("• <b>Dual Target Engine:</b> Handles FQDNs & raw IPv4/IPv6 with reverse PTR<br/>• <b>Infrastructure Intelligence:</b> Autonomous System Number (ASN) & ISP<br/>• <b>Security Fingerprinting:</b> Automatically detects Cloudflare WAF / AWS / GCP<br/>• <b>Multi-Platform CLI:</b> Verified setup for Kali Linux, Windows & macOS<br/>• <b>Audit Export:</b> Automatically saves structured JSON deliverable in <code>reports/</code>", body_style)
        ]
    ]
    scope_table = Table(scope_data, colWidths=[230, 310])
    scope_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#e0f2fe")),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#93c5fd")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#bfdbfe")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(scope_table)
    story.append(Spacer(1, 6))

    # 4. Practical Scan Findings Table
    story.append(Paragraph("2. Passive Reconnaissance Intelligence Findings", h2_style))
    findings_data = [
        [Paragraph("Category", meta_label), Paragraph("Observed Value", meta_label), Paragraph("Security / Threat Implications", meta_label)],
        [Paragraph("Target Host", meta_val), Paragraph("example.com", meta_val), Paragraph("Authorized RFC 2606 lab testing domain", meta_val)],
        [Paragraph("Resolved IPv4", meta_val), Paragraph("104.20.23.154", meta_val), Paragraph("Anycast IP fronting Cloudflare edge infrastructure", meta_val)],
        [Paragraph("WHOIS Registrar", meta_val), Paragraph("RESERVED-Internet Assigned Numbers Authority", meta_val), Paragraph("Identifies registrar ownership; renewal 2027-08-13", meta_val)],
        [Paragraph("Name Servers", meta_val), Paragraph("ELLIOTT.NS.CLOUDFLARE.COM<br/>HERA.NS.CLOUDFLARE.COM", meta_val), Paragraph("Confirms authoritative DNS managed by Cloudflare", meta_val)],
        [Paragraph("Geolocation", meta_val), Paragraph("Toronto, Ontario, Canada (43.65, -79.38)", meta_val), Paragraph("Identifies edge point of presence (PoP) location", meta_val)],
        [Paragraph("Network / ASN", meta_val), Paragraph("AS13335 (Cloudflare, Inc.)", meta_val), Paragraph("Enterprise CDN protecting origin servers against direct DDoS", meta_val)],
        [Paragraph("Security Posture", meta_val), Paragraph("Cloudflare WAF / Reverse Proxy Protection", meta_val), Paragraph("Direct port scanning on domain IP hits WAF, not origin server", meta_val)],
    ]
    findings_table = Table(findings_data, colWidths=[90, 185, 265])
    findings_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#f1f5f9")),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(findings_table)
    story.append(Spacer(1, 6))

    # 5. Attacker vs. Defender Analysis
    story.append(Paragraph("3. Attacker vs. Defender Perspective", h2_style))
    analysis_text = """
    <b>Adversary Perspective (Red Team / Social Engineering):</b> Passive reconnaissance allows attackers to map target architecture without triggering Security Information and Event Management (SIEM) alerts. Identifying domain registrars and expiration windows enables domain squatting and spear-phishing prep. Uncovering ASN details reveals whether an organization relies on third-party cloud SaaS or on-premises servers.<br/><br/>
    <b>Defender Perspective (Blue Team):</b> Defenders must ensure WHOIS privacy is strictly enforced, audit public DNS records regularly, and verify that external cloud/WAF configurations do not expose origin server IP addresses.
    """
    story.append(Paragraph(analysis_text, body_style))
    story.append(Spacer(1, 8))

    footer_page1 = "<font color='#64748b' size='7.5'><i>Page 1 of 2 — Sqrock IT Solution Alpha 2 Cybersecurity Track • Evaluated Deliverable</i></font>"
    story.append(Paragraph(footer_page1, body_style))

    # ------------------ PAGE 2: Practical Evidence & Screenshots ------------------
    story.append(PageBreak())

    story.append(Paragraph("4. Practical Execution Proof (Terminal Screenshots & Setup)", h2_style))
    story.append(Paragraph("The following screenshots verify live execution of PEER'S OSINT Scanner against the authorized practice domain (example.com), as well as multi-platform installation documentation:", body_style))
    story.append(Spacer(1, 6))

    img1_path = "screenshots/peer_scan_terminal_part1.png"
    img2_path = "screenshots/peer_scan_terminal_part2.png"
    img3_path = "screenshots/peer_scan_kali_guide.png"

    if os.path.exists(img1_path):
        story.append(Image(img1_path, width=530, height=180))
        story.append(Spacer(1, 6))
    if os.path.exists(img2_path):
        story.append(Image(img2_path, width=530, height=130))
        story.append(Spacer(1, 6))
    if os.path.exists(img3_path):
        story.append(Image(img3_path, width=530, height=170))
        story.append(Spacer(1, 8))

    footer_page2 = "<font color='#64748b' size='7.5'><i>Page 2 of 2 — Script outputs and practical execution logs strictly follow IT Act 2000 & CFAA authorized educational lab guidelines.</i></font>"
    story.append(Paragraph(footer_page2, body_style))

    doc.build(story)
    print(f"[+] Executive PDF Report created successfully at: {output_pdf_path}")

if __name__ == "__main__":
    create_report()
