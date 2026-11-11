from pathlib import Path

from dotenv import load_dotenv

# Sunucuyu Inspector ya da Claude Desktop başlatınca --env-file verilmiyor.
# Bu yüzden proje kökündeki .env'yi burada, diğer importlardan önce yüklüyoruz.
load_dotenv(Path(__file__).resolve().parents[2] / ".env")

# mcp 2.x: FastMCP'nin yeni adı MCPServer (API'si aynı)
from mcp.server.mcpserver import MCPServer  # noqa: E402

from job_fit_agent.graph import analyze  # noqa: E402
from job_fit_agent.profile import my_profile  # noqa: E402

# DİKKAT: Bu sunucu stdout üzerinden konuşur. Burada ya da çağrılan kodda print
# kullanma; debug için print(..., file=sys.stderr) kullan.

mcp = MCPServer("job-fit-agent")


@mcp.tool()
def analyze_job_posting(job_text: str) -> str:
    """Bir iş ilanını kullanıcının profiliyle karşılaştırır.

    İlandaki becerileri çıkarır, her biri için kullanıcıda var / kısmen / yok
    kararı verir ve eksikler için öncelikli bir çalışma planı hazırlar. Sonucu
    Markdown formatında bir eşleşme raporu olarak döndürür.

    Ne zaman kullanılır: Kullanıcı bir iş ilanı paylaşıp bu ilana ne kadar
    uygun olduğunu, hangi becerilerinin eksik olduğunu ya da neye çalışması
    gerektiğini sorduğunda.

    Girdi: İlanın tam metni. Özet ya da yalnızca başlık verme; beceriler ve
    gereksinimler metnin tamamından çıkarılıyor.

    Süre: Yaklaşık 25 saniye sürer. Çağırmadan önce kullanıcıya analizin biraz
    zaman alacağını söyle.

    Args:
        job_text: İş ilanının tam metni.
    """
    return analyze(job_text, my_profile)


if __name__ == "__main__":
    mcp.run()
