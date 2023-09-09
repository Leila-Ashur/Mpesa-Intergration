class CommentsListView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
    


class CommentsListView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Corrected status code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Corrected status code

class CommentsDetailView  (APIView):
    def get(self,request,id,format= None):
        comment=Comments.objects.get(id=id)
        serializer= CommentsSerializer(customer)
        return Response(serializer.data)
        

    def put (self,request,id,format=None):
        comment=Comment.objects.get(id=id)
        serializer=CustomerSerializer(comment,request.data)
        if serializer.is_valid():
            serializer.save()
           
            return Response(serializer.errors,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


        
           


    def Delete(self,request,id,format=None)  :
        comment=Comment.objects.get(id=id)       
        comment.delete()
        return Response ("comment deleted",status=status.HTTP_204_NO_CONTENT)
