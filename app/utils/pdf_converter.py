import asyncio
from pathlib import Path
import subprocess
import os

async def convert_to_pdf(pptx_path: Path) -> Path:
    """
    Convert PPTX to PDF using LibreOffice in headless mode
    """
    output_dir = pptx_path.parent
    pdf_path = output_dir / f"{pptx_path.stem}.pdf"
    
    # Command to convert using LibreOffice
    cmd = [
        'libreoffice',
        '--headless',
        '--convert-to',
        'pdf',
        '--outdir',
        str(output_dir),
        str(pptx_path)
    ]
    
    # Run conversion process
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    
    # Wait for conversion to complete
    stdout, stderr = await process.communicate()
    
    if process.returncode != 0:
        raise Exception(f"PDF conversion failed: {stderr.decode()}")
    
    return pdf_path 