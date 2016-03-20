package org.liufeng.course.servlet;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.liufeng.course.service.CoreService;
import org.liufeng.course.util.MySignUtil;
import org.liufeng.course.util.SignUtil;

import com.qq.weixin.mp.aes.AesException;
import com.qq.weixin.mp.aes.WXBizMsgCrypt;

/**
 * 核心请求处理类
 * 
 * @author liufeng
 * @date 2013-05-18
 */
public class CoreServlet extends HttpServlet {
	private static final long serialVersionUID = 4440739483644821986L;
		
	/**
	 * 确认请求来自微信服务器
	 */
	
	public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		// 微信加密签名
		String msg_Signature = request.getParameter("msg_signature");
		// 时间戳
		String timeStamp = request.getParameter("timestamp");
		// 随机数
		String nonce = request.getParameter("nonce");
		//加密字符串
		String echoStr = request.getParameter("echostr");

		PrintWriter out = response.getWriter();
		// 通过检验signature对请求进行校验，若校验成功则原样返回echostr，表示接入成功，否则接入失败
		try {
			echoStr=MySignUtil.wxcpt.VerifyURL(msg_Signature, timeStamp, nonce, echoStr);
		} catch (AesException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
			out.print(echoStr);
	}

	/**
	 * 处理微信服务器发来的消息
	 */
	public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// 将请求、响应的编码均设置为UTF-8（防止中文乱码）
		request.setCharacterEncoding("UTF-8");
		response.setCharacterEncoding("UTF-8");
		
		// 微信加密签名
				String msg_Signature = request.getParameter("msg_signature");
				// 时间戳
				String timeStamp = request.getParameter("timestamp");
				// 随机数
				String nonce = request.getParameter("nonce");
				//加密字符串
				String echoStr = request.getParameter("echostr");

				// 通过检验signature对请求进行校验，若校验成功则原样返回echostr，表示接入成功，否则接入失败
				try {
					echoStr=MySignUtil.wxcpt.DecryptMsg(msg_Signature, timeStamp, nonce, echoStr);
				} catch (AesException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}

		// 调用核心业务类接收消息、处理消息
		String respMessage = CoreService.processRequest(request);
		
		// 响应消息
		PrintWriter out = response.getWriter();
		out.print(respMessage);
		out.close();
	}

}
