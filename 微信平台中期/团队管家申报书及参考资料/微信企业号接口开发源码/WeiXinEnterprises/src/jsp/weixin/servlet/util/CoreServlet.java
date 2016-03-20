package jsp.weixin.servlet.util;
/**
 * @author Engineer-Jsp
 * @date 2014.09.23
 * ����Servlet��*/
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.apache.commons.io.IOUtils;
import jsp.weixin.ParamesAPI.util.ParamesAPI;
import jsp.weixin.encryption.util.AesException;
import jsp.weixin.encryption.util.WXBizMsgCrypt;
import jsp.weixin.servicet.util.CoreService;
public class CoreServlet extends HttpServlet{
	/**
	 * 
	 */
	private static final long serialVersionUID = 4440739483644821986L;
	
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// ΢�ż���ǩ��  
        String msg_signature = request.getParameter("msg_signature");  
        // ʱ���  
        String timestamp = request.getParameter("timestamp");  
        // �����  
        String nonce = request.getParameter("nonce");  
        // ����ַ���  
        String echostr = request.getParameter("echostr");  
        // ��ӡ�����ַ
        System.out.println("request=" + request.getRequestURL());  
        // ��
        PrintWriter out = response.getWriter();  
        // ͨ������signature���������У�飬��У��ɹ���ԭ������echostr����ʾ����ɹ����������ʧ��  
        String result = null;  
        try {  
        	WXBizMsgCrypt wxcpt = new WXBizMsgCrypt(ParamesAPI.token,ParamesAPI.encodingAESKey,ParamesAPI.corpId);  
        	// ��֤URL����
        	result = wxcpt.VerifyURL(msg_signature, timestamp, nonce, echostr);  
        } catch (AesException e) {  
            e.printStackTrace();  
        }  
        if (result == null) {  
        	// resultΪ�գ�����token
        	result = ParamesAPI.token;
        }
        // ƴ���������
        String str = msg_signature+" "+timestamp+" "+nonce+" "+echostr;
        // ��ӡ����+��ַ+result
        System.out.println("Exception:"+result+" "+ request.getRequestURL()+" "+"FourParames:"+str);
        out.print(result);
        out.close();  
        out = null;  
	}
	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
//		 ��������Ӧ�ı��������ΪUTF-8����ֹ�������룩
		request.setCharacterEncoding("UTF-8");
		response.setCharacterEncoding("UTF-8");

		// ΢�ż���ǩ��
		String msg_signature = request.getParameter("msg_signature");
		// ʱ���
		String timestamp = request.getParameter("timestamp");
		// �����
		String nonce = request.getParameter("nonce");
		
		//�������ж�ȡ����post����
		InputStream inputStream = request.getInputStream();
		//commons.io.jar ����
		String Post = IOUtils.toString(inputStream, "UTF-8");
		// Post��ӡ���
		System.out.println(Post);
		
		String Msg = "";
		WXBizMsgCrypt wxcpt = null;
		try {
			wxcpt = new WXBizMsgCrypt(ParamesAPI.token,ParamesAPI.encodingAESKey,ParamesAPI.corpId);
			//������Ϣ
			Msg = wxcpt.DecryptMsg(msg_signature, timestamp, nonce, Post);
		} catch (AesException e) {
			e.printStackTrace();
		}
		// Msg��ӡ���
		System.out.println("Msg��ӡ�����" + Msg);
		
		// ���ú���ҵ���������Ϣ��������Ϣ
		String respMessage = CoreService.processRequest(Msg);
		
		// respMessage��ӡ���
		System.out.println("respMessage��ӡ�����" + respMessage);
		String encryptMsg = "";
		try {
			//���ܻظ���Ϣ
			encryptMsg = wxcpt.EncryptMsg(respMessage, timestamp, nonce);
		} catch (AesException e) {
			e.printStackTrace();
		}
		
		// ��Ӧ��Ϣ
		PrintWriter out = response.getWriter();
		out.print(encryptMsg);
		out.close();
	}

}
