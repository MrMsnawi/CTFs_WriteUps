we open it in .docx editor but we don't see anything interisting:
```
Observation of emergent behavior in autonomous systems remains a primary focus of our lab. This report summarizes recent experiments, proposed ethical controls, and suggested directions for improving transparency with human stakeholders.

Historically, ethical frameworks have evolved in reaction to new technologies rather than proactively. To prevent harm, we recommend adopting iterative review cycles that include diverse student perspectives.

Practically, implementing transparency requires both technical and organizational changes. Instrumentation, clear logging standards, and reproducible evaluation pipelines are foundational steps.

Xenial collaboration models, where designers, users, and ethicists iteratively work together — produce more robust safeguards than ad-hoc oversight. The lab has trialed weekly cross-disciplinary meetings with encouraging early results.

Recent experiments conducted in the lab indicate that explainability features increase user trust, but can also leak sensitive model behavior if not carefully scoped. We include example transcripts in the appendix.

Likewise, student feedback highlighted concerns over identifiable data being surfaced inadvertently by visualization tools. We propose default redaction layers in public reports.

Regulatory considerations suggest we prioritize consent and data minimization. Any shared dataset should have an attached data-use agreement and a renewal schedule for consent validation.

Finally, the appendix contains raw data logs, supplementary charts, and encrypted artifacts for internal review. Please follow the lab’s data-handling guidelines when accessing archived files.
```
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files$ unzip OSU_Ethics_Report.docx -d docx_contents
Archive:  OSU_Ethics_Report.docx
  inflating: docx_contents/[Content_Types].xml  
  inflating: docx_contents/_rels/.rels  
  inflating: docx_contents/docProps/app.xml  
  inflating: docx_contents/docProps/core.xml  
  inflating: docx_contents/docProps/custom.xml  
  inflating: docx_contents/word/_rels/document.xml.rels  
  inflating: docx_contents/word/document.xml  
  inflating: docx_contents/word/fontTable.xml  
  inflating: docx_contents/word/settings.xml  
  inflating: docx_contents/word/styles.xml  
  inflating: docx_contents/word/theme/theme1.xml  
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files$ ls
docx_contents  OSU_Ethics_Report.docx
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files$ cd docx_contents/
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents$ ls
'[Content_Types].xml'   docProps   _rels   word
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents$ cat \[Content_Types\].xml 
<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="xml" ContentType="application/xml"/><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="png" ContentType="image/png"/><Default Extension="jpeg" ContentType="image/jpeg"/><Override PartName="/_rels/.rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/><Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/><Override PartName="/docProps/custom.xml" ContentType="application/vnd.openxmlformats-officedocument.custom-properties+xml"/><Override PartName="/word/_rels/document.xml.rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/><Override PartName="/word/fontTable.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml"/><Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/><Override PartName="/word/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>
</Types>ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents$ cat \[Content_Types\].xml | grep bctf
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents$ 
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents$ cd docProps/
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/docProps$ ls
app.xml  core.xml  custom.xml
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/docProps$ cat * | grep bctf
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/docProps$ cat *
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"><Template></Template><TotalTime>22</TotalTime><Application>LibreOffice/24.2.7.2$Linux_X86_64 LibreOffice_project/420$Build-2</Application><AppVersion>15.0000</AppVersion><Pages>1</Pages><Words>210</Words><Characters>1442</Characters><CharactersWithSpaces>1645</CharactersWithSpaces><Paragraphs>8</Paragraphs></Properties><?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dcterms:created xsi:type="dcterms:W3CDTF">2025-11-04T15:29:37Z</dcterms:created><dc:creator></dc:creator><dc:description></dc:description><dc:language>en-US</dc:language><cp:lastModifiedBy></cp:lastModifiedBy><dcterms:modified xsi:type="dcterms:W3CDTF">2025-11-06T18:19:56Z</dcterms:modified><cp:revision>3</cp:revision><dc:subject></dc:subject><dc:title></dc:title></cp:coreProperties><?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/custom-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"></Properties>ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/docProps$ cd ..
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents$ ls
'[Content_Types].xml'   docProps   _rels   word
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents$ cd _rels/
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/_rels$ ls
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/_rels$ ls
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/_rels$ 
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/_rels$ 
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/_rels$ cd ..
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents$ ls
'[Content_Types].xml'   docProps   _rels   word
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents$ cd word/
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/word$ ls
document.xml  fontTable.xml  _rels  settings.xml  styles.xml  theme
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/word$ cat * | grep bctf
cat: _rels: Is a directory
cat: theme: Is a directory
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/word$ cat document.xml | grep bctf
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/word$ cat *.xml | grep bctf
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/word$ cd _rels/
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/word/_rels$ ls
document.xml.rels
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/word/_rels$ cat document.xml.rels 
<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/fontTable" Target="fontTable.xml"/><Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/><Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="theme/theme1.xml"/>
</Relationships>ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/word/_rels$ cat documenp bctfrels | gre 
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/word/_rels$ cat document.xml.rels | grep bctf
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/word/_rels$ 
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/word/_rels$ 
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/word/_rels$ cd ..
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/word$ ls
document.xml  fontTable.xml  _rels  settings.xml  styles.xml  theme
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/word$ cd theme/
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/word/theme$ ls
theme1.xml
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/word/theme$ cat theme1.xml 
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="ProfessorTheme_Loud">
  <a:themeElements>
    <a:clrScheme name="CustomLoud">
      <a:dk1><a:srgbClr val="1F1F1F"/></a:dk1>
      <a:lt1><a:srgbClr val="FFFFFF"/></a:lt1>
      <a:dk2><a:srgbClr val="2B2B2B"/></a:dk2>
      <a:lt2><a:srgbClr val="F4F4F4"/></a:lt2>

      <a:accent1><a:srgbClr val="FF4500"/></a:accent1>  <!-- vivid orange -->
      <a:accent2><a:srgbClr val="0066CC"/></a:accent2>  <!-- strong blue -->
      <a:accent3><a:srgbClr val="8A2BE2"/></a:accent3>  <!-- bright purple -->
      <a:accent4><a:srgbClr val="228B22"/></a:accent4>  <!-- strong green -->
      <a:accent5><a:srgbClr val="FFD700"/></a:accent5>  <!-- gold -->
      <a:accent6><a:srgbClr val="DC143C"/></a:accent6>  <!-- crimson -->
      <!-- bctf{docx_is_zip} -->

      <a:hlink><a:srgbClr val="0000FF"/></a:hlink>
      <a:folHlink><a:srgbClr val="800080"/></a:folHlink>
    </a:clrScheme>

    <a:fmtScheme name="CustomFmt">

      <a:fillStyleLst>
        <a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill>
      </a:fillStyleLst>
      <a:lnStyleLst/>
      <a:effectStyleLst/>
    </a:fmtScheme>
  </a:themeElements>

  <a:objectDefaults/>
  <a:extraClrSchemeLst/>
</a:theme>
ousen@0u5en:~/Desktop/CTFs_WriteUps/BuckeyeCTF_2025/beginner/The_professors_files/docx_contents/word/theme$ cat theme1.xml | grep bctf
      <!-- bctf{docx_is_zip} -->

