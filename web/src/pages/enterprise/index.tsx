import ChatContainer from '@/pages/chat/chat-container';
import FileUploader from '@/components/file-uploader';
import { Flex } from 'antd';

const EnterprisePage = () => {
  return (
    <Flex className="p-4 gap-4" vertical>
      <h1 className="text-2xl font-bold">Enterprise RAG Interface</h1>
      <div className="bg-card p-4 rounded-md shadow">
        <h2 className="font-semibold mb-2">Upload Documents</h2>
        <FileUploader multiple className="mb-4" />
      </div>
      <div className="bg-card p-4 rounded-md shadow flex-1">
        <h2 className="font-semibold mb-2">Chat</h2>
        <ChatContainer controller={new AbortController()} />
      </div>
    </Flex>
  );
};

export default EnterprisePage;
