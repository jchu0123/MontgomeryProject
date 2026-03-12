$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:8000/")
$listener.Start()
Write-Host "Listening on http://localhost:8000/"

try {
    while ($listener.IsListening) {
        $context = $listener.GetContext()
        $request = $context.Request
        $response = $context.Response
        
        $localPath = "c:\Users\jchu0\OneDrive\Documents\MontgomeryProject\SchoolDetails" + $request.Url.LocalPath.Replace("/", "\")
        if ($request.Url.LocalPath -eq "/") { $localPath = "c:\Users\jchu0\OneDrive\Documents\MontgomeryProject\SchoolDetails\index.html" }
        
        try {
            if (Test-Path $localPath -PathType Leaf) {
                # Add basic content types for html
                if ($localPath.EndsWith(".html")) { $response.ContentType = "text/html" }
                
                $content = [System.IO.File]::ReadAllBytes($localPath)
                $response.ContentLength64 = $content.Length
                $response.OutputStream.Write($content, 0, $content.Length)
            } else {
                $response.StatusCode = 404
            }
        } catch {
            $response.StatusCode = 500
        }
        
        $response.Close()
    }
} finally {
    $listener.Stop()
}
