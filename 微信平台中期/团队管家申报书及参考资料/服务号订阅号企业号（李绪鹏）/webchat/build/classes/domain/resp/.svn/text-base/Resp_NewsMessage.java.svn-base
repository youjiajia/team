package domain.resp;

import java.util.List;

import domain.Article;

/**
 * 文本消息
 * 
 * @author 李绪鹏
 * @date 2014-10-25
 * <xml>
   <ToUserName><![CDATA[toUser]]></ToUserName>
   <FromUserName><![CDATA[fromUser]]></FromUserName>
   <CreateTime>12345678</CreateTime>
   <MsgType><![CDATA[news]]></MsgType>
   <ArticleCount>2</ArticleCount>
   <Articles>
       <item>
           <Title><![CDATA[title1]]></Title> 
           <Description><![CDATA[description1]]></Description>
           <PicUrl><![CDATA[picurl]]></PicUrl>
           <Url><![CDATA[url]]></Url>
       </item>
       <item>
           <Title><![CDATA[title]]></Title>
           <Description><![CDATA[description]]></Description>
           <PicUrl><![CDATA[picurl]]></PicUrl>
           <Url><![CDATA[url]]></Url>
       </item>
   </Articles>
</xml>
 */
public class Resp_NewsMessage extends Resp_BaseMessage {
	// 	图文条数，默认第一条为大图。图文数不能超过10，否则将会无响应 
	private int articleCount;
	// 多条图文消息信息，默认第一个item为大图
	private List<Article> articles;
	

	public Resp_NewsMessage() {
		super();
		this.setMsgType(RESP_MESSAGE_TYPE_NEWS);
	}

	public int getArticleCount() {
		return articleCount;
	}

	public void setArticleCount(int articleCount) {
		this.articleCount = articleCount;
	}

	public List<Article> getArticles() {
		return articles;
	}

	public void setArticles(List<Article> articles) {
		this.articles = articles;
	}
}