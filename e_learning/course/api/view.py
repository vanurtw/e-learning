from rest_framework import generics
from .serializer import SubjectSerializer, CourseSerializer, CourseWithContentsSerializer
from course.models import Subject, Course
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from .permissions import IsEnrolled


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


# class CourseEnrollView(APIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request, pk, format=None):
#         course = get_object_or_404(Course, pk=pk)
#         course.students.add(request.user)
#         return Response({'enrolled': True})


class ViewSetCourse(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated],
            authentication_classes=[BasicAuthentication])
    def enroll(self, requesst, *args, **kwargs):
        course = self.get_object()
        course.students.add(requesst.user)
        return Response({'enroll': 'True'})

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated, IsEnrolled],
            authentication_classes=[BasicAuthentication], serializer_class=CourseWithContentsSerializer)
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
