package domain.event;
/**
 * 关注/取消关注事件的推送
 * 这个地方Event应该自己设置
 * @author 李绪鹏
 * @date 2014-10-25
 *<xml>
   <ToUserName><![CDATA[toUser]]></ToUserName>
   <FromUserName><![CDATA[UserID]]></FromUserName>
   <CreateTime>1348831860</CreateTime>
   <MsgType><![CDATA[event]]></MsgType>
   <Event><![CDATA[subscribe]]></Event>
   <AgentID>1</AgentID>
</xml>
 */
public class SubscribeEvent extends BaseEvent {
}
