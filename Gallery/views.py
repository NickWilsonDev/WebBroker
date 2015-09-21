from django.shortcuts import render, get_object_or_404
from models import Gallery, GalleryForm
from convertImage import create_thumbnail_from_image_field
from django.contrib.auth.decorators import login_required

# Create your views here.


def gallery(request):
    """ 
        This view is what any visitor to the site can see, it just renders a
        template with the all the uploaded images 'attached'
    """
    images = Gallery.objects.order_by('pk')
    return render(request, 'Gallery/gallery.html', {'images': images})


@login_required
def addImage(request):
    """
        This view allows an user, who is logged in, to upload an image that 
        will be added to the gallery
    """
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery.save()
            create_thumbnail_from_image_field(gallery.image, gallery.thumbnail, 200, 200)
            gallery.save()
            images = Gallery.objects.order_by('pk')
            return render(request, 'Gallery/listImages.html', {'images': images})
        else:
            print "Form was not valid"
            print form.errors
    else:
        form = GalleryForm()
    return render(request, 'Gallery/addImage.html', {'form': form})


@login_required
def listImages(request):
    """
        This view will render a template that lists all of the currently
        uploaded images and give the user options to delete or edit images.
    """
    images = Gallery.objects.order_by('pk')
    return render(request, 'Gallery/listImages.html', {'images': images})

@login_required
def imageEdit(request, pk):
    """
        This view will render a template that allows the user to edit details
        of the uploaded image.
    """
    image = get_object_or_404(Gallery, pk=pk)
    if request.method == "POST":
        form = GalleryForm(request.POST, instance=image)
        if form.is_valid():
            image = form.save(commit=False)
            image.save()
            images = Gallery.objects.order_by('pk')
            return render(request,'Gallery/listImages.html', {'images': images})
    else:
        form = GalleryForm(instance=image)
    return render(request, 'Gallery/imageEdit.html', {'form': form})

    
@login_required
def imageDelete(request, pk):
    """
        This view will allow an user to delete an uploaded image.
    """
    image = get_object_or_404(Gallery, pk=pk)
    image.delete()
    images = Gallery.objects.order_by('pk')
    return render(request, 'Gallery/listImages.html', {'images': images})
